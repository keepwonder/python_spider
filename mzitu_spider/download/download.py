#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : download.py 
# @time  : 2017/09/26 13:23:35
# @description：to be filled
import urllib.request
import time


class DownHtml(object):
    def __init__(self):
        pass

    def download_html(self, url):
        """
        下载每一个页面，请求头Referer参数设置，处理防盗链
        :param url:
        :return:
        """
        time.sleep(0.25)

        if url is None:
            return None

        req = urllib.request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
                       )
        req.add_header('Referer', 'http://www.mzitu.com/')

        response = urllib.request.urlopen(req)

        if response.getcode() != 200:
            return None

        return response

# if __name__ == '__main__':
#
#     main_page = DownHtml().download_html('http://www.mzitu.com')
#     print(main_page)
