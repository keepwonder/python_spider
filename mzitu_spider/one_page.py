#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : one_page.py 
# @time  : 2017/09/26 17:26:35
# @description：to be filled

import urllib.request
from bs4 import BeautifulSoup

url = 'http://i.meizitu.net/2017/09/25a02.jpg'

heads = {'Referer': 'http://www.mzitu.com/103840/3'}
req = urllib.request.Request(url, headers=heads)
res = urllib.request.urlopen(req)
with open('a.jpg', 'wb') as f:
    f.write(res.read())
