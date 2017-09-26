#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : download.py 
# @time  : 2017/09/23 13:19:58
# @description：下载器

from urllib import request, error
import time


class DownloadHtml(object):
    def __init__(self):
        pass

    def download(self, url):
        time.sleep(3)

        try:
            # if url is None:
            #     return None
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) ' \
                         'AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
            head = {'User-Agent': user_agent}
            req = request.Request(url, headers=head)
            res = request.urlopen(req)
            # if res.get_code() != 200:
            #     return None
            return res.read().decode('utf-8')

        except error.URLError as e:
            if hasattr(e, 'code'):
                print(e.code)
            if hasattr(e, 'reason'):
                print('reason:', e.reason)
