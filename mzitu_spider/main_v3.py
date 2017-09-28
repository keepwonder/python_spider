#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : main.py 
# @time  : 2017/09/26 13:23:13
# @description：版本3，加入MongoDB数据库，保存相关信息
from python_spider_action.mzitu_spider.parse import parse_v3
from python_spider_action.mzitu_spider.util import makedir, mongoUtil


class MzituSpider(object):
    def __init__(self):
        self.parse = parse_v3.ParseHtml()
        # self.mkdir = makedir.MakeDir()
        # self.dbclient = mongoUtil().connect_mongo()  # 连接本地MongoDB
        # self.picdb = self.dbclient.girl_gallery  # 建立girl_gallery数据库
        # self.picset = self.picdb.girl_pic  # 建立girl_pic集合(相关于表结构)
        # self.title = ''  # 保存页面主题
        # self.url = ''  # 保存页面地址
        # self.img_urls = []  # 初始化一个列表，用来保存图片地址

    def get_img(self, root_url):
        self.parse.parse_main_page(root_url)
        # all_a = self.parse.parse_main_page(root_url)
        # for a in all_a:
        #     title = a.get_text()
        #     self.title = title  # 将主题保存到self.title中
        #     print('开始保存：'.format(title))
        #     path = str(title)
        #     self.mkdir.makedirs(path)
        #     href = a['href']
        #     self.url = href  # 将页面地址保存到self.url中
        #     if self.picset.findOne({'主题页面': href}):
        #         print('该页面已经爬取过')
        #     else:
        #         self.parse.parse_single_page(href)


if __name__ == '__main__':
    url = 'http://www.mzitu.com/all/'
    MzituSpider().get_img(url)
