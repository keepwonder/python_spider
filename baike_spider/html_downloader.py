#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : html_downloader.py
# @time  : 2017/09/09 20:48:27
# @description：下载器
import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read().decode('utf-8')
