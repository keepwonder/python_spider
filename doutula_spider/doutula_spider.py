#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : doutula_spider.py
# @time  : 2017/10/03 00:15:57
# @description：to be filled
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import os

# 获取所有页面url
BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = []
for i in range(1, 1008):
    PAGE_URL_LIST.append(BASE_PAGE_URL + str(i))


# 下载图片
def download_img(url):
    split_list = url.split('/')
    filename = split_list[-1]
    path = os.path.join('images', filename)
    urlretrieve(url, filename=path)


# img = requests.get('http://ww1.sinaimg.cn/bmiddle/6af89bc8gw1f8nserjkc4g203s03sglw.gif')
# with open('a.gif', 'ab') as f:
#     f.write(img.content)

# 获取每一页内容
def get_page(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'lxml')
    img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
    for img in img_list:
        url = img['data-original']
        download_img(url)
        # print(img['data-original'])


def main():
    for page_url in PAGE_URL_LIST:
        get_page(page_url)


if __name__ == '__main__':
    main()
