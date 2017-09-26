#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : test.py 
# @time  : 2017/09/26 13:44:53
# @description：to be filled

import urllib.request
from bs4 import BeautifulSoup
import os

root_url = 'http://www.mzitu.com/all/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'Connection': 'Keep-Alive',
    'Referer': 'http://www.mzitu.com/'
}
req = urllib.request.Request(root_url, headers=headers)

response = urllib.request.urlopen(req)
res = urllib.request.urlopen(req)

soup = BeautifulSoup(res, 'lxml')
all_a = soup.find('div', class_='all').find_all('a')
for a in all_a:
    title = a.get_text()
    path = str(title).strip()  # 去掉空格
    os.makedirs(os.path.join('/Users/jockie/Documents/mzitu', path))
    os.chdir('/Users/jockie/Documents/mzitu/' + path)
    href = a['href']
    req_a = urllib.request.Request(href, headers=headers)
    html = urllib.request.urlopen(req_a)
    html_soup = BeautifulSoup(html, 'lxml')
    max_page = html_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1, int(max_page) + 1):
        page_url = href + '/' + str(page)
        req_b = urllib.request.Request(page_url, headers=headers)
        img_html = urllib.request.urlopen(req_b)
        img_soup = BeautifulSoup(img_html, 'lxml')
        img_url = img_soup.find('div', class_='main-image').find('img')['src']
        name = img_url[-9:-4]  # 取URL 倒数第四至第九位 做图片的名字
        req_c = urllib.request.Request(img_url, headers=headers)
        # req_c.add_header('Referer', page_url)
        img = urllib.request.urlopen(req_c)
        with open(name + '.jpg', 'wb') as f:
            f.write(img.read())
            # print(img_url)
            # print(page_url)
            # print(max_page)
            # print(title, href)
