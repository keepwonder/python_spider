#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : util.py
# @time  : 2017/09/26 20:46:19
# @description：to be filled
from python_spider_action.mzitu_spider.download import download_v3


class SaveImg(object):
    def __init__(self):
        pass

    def saveImg(self, img_url):
        """
        保存图片
        :param img_url: http://i.meizitu.net/2017/09/25b01.jpg
        :return: 保存文件到目录
        """
        name = img_url[-9:-4]
        img = download_v3.DownHtml().download_html(img_url, 3)
        with open(name + '.jpg', 'ab') as f:
            print('开始保存{}.jpg'.format(name))
            f.write(img.content)
