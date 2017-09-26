#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : down_html.py 
# @time  : 2017/09/23 23:54:05
# @description：下载器
import time
import urllib.request


class DownHtml(object):
    def __init__(self):
        pass

    def download(self, url):
        time.sleep(3)

        if url is None or url == '':
            return None

        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)

        if response.get_code() != 200:
            return None

        return response.read()
