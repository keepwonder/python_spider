#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : main.py 
# @time  : 2017/09/26 13:23:13
# @description：版本3，加入MongoDB数据库，保存相关信息，去除重复下载
from python_spider_action.mzitu_spider.parse import parse_v3
import time


class MzituSpider(object):
    def __init__(self):
        # self.parse = parse_v3.ParseHtml()
        pass

    def get_img(self, root_url):
        # self.parse.parse_main_page(root_url)
        parse_v3.ParseHtml().parse_main_page(root_url)


if __name__ == '__main__':
    url = 'http://www.mzitu.com/all/'
    begin = time.time()
    MzituSpider().get_img(url)
    end = time.time()
    print('花费时间:{}min'.format((end - begin) / 60))
