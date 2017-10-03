#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : doutula_spider.py
# @time  : 2017/10/03 00:15:57
# @description：多线程爬取
import requests
from urllib import request, error
from bs4 import BeautifulSoup
import os
import threading

# 获取所有页面url
BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
# 页面url列表
PAGE_URL_LIST = []
# 所有表情的url列表
FACE_URL_LIST = []
for i in range(1, 1008):
    PAGE_URL_LIST.append(BASE_PAGE_URL + str(i))
# 全局锁
gLock = threading.Lock()


def download_page(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
    }
    return requests.get(url, headers=header)


def auto_down(url, filename):
    try:
        request.urlretrieve(url, filename)
    except error.ContentTooShortError:
        print('Network conditions is not good.Reloading.')
        auto_down(url, filename)
    except error.HTTPError as http_err:
        print(http_err.url)


def producer():
    while True:
        gLock.acquire()
        if len(PAGE_URL_LIST) == 0:
            gLock.release()
            break
        else:
            page_url = PAGE_URL_LIST.pop()
            gLock.release()
            response = download_page(page_url)
            content = response.content
            soup = BeautifulSoup(content, 'lxml')
            img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
            gLock.acquire()
            for img in img_list:
                url = img['data-original']
                if not url.startswith('http'):
                    url = 'http:' + url
                FACE_URL_LIST.append(url)
            gLock.release()


def consumer():
    while True:
        gLock.acquire()
        if len(FACE_URL_LIST) == 0:
            gLock.release()
            continue
        else:
            face_url = FACE_URL_LIST.pop()
            gLock.release()
            split_list = face_url.split('/')
            filename = split_list[-1]
            path = os.path.join('img', filename)
            auto_down(face_url, filename=path)


def main():
    # 创建8个线程作为生产者，去爬取表情url
    for _ in range(8):
        p = threading.Thread(target=producer)
        p.start()

    # 创建8个线程作为消费者，去把表情图片下载下来
    for _ in range(8):
        c = threading.Thread(target=consumer)
        c.start()


if __name__ == '__main__':
    main()
