#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : train_spider.py 
# @time  : 2017/09/23 13:25:08
# @description：to be filled

from python_spider_action.qiubai_spider.download import download
from python_spider_action.qiubai_spider.parse import parse


class QiuBaiSpider(object):
    def __init__(self):
        self.download_page = download.DownloadHtml()
        self.parse_page = parse.ParseHtml()

    def down_page(self, url):
        return self.download_page.download(url)

    def get_content(self, content):
        return self.parse_page.parse(content)


if __name__ == '__main__':
    root_url = 'https://www.qiushibaike.com/hot/'
    spider = QiuBaiSpider()
    page = spider.down_page(root_url)
    context = spider.get_content(page)
