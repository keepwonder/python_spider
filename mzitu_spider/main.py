#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : main.py 
# @time  : 2017/09/26 13:23:13
# @description：to be filled
from python_spider_action.mzitu_spider.parse import parse
from python_spider_action.mzitu_spider.util import makedir


class MzituSpider(object):
    def __init__(self):
        self.parse = parse.ParseHtml()
        self.mkdir = makedir.MakeDir()

    def get_img(self, root_url):
        all_a = self.parse.parse_main_page(root_url)
        for a in all_a:
            title = a.get_text()
            path = str(title)
            self.mkdir.makedirs(path)
            href = a['href']
            self.parse.parse_single_page(href)


if __name__ == '__main__':
    url = 'http://www.mzitu.com/all/'
    MzituSpider().get_img(url)
