#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : mongoUtil.py 
# @time  : 2017/09/27 23:10:39
# @description：to be filled

from pymongo import MongoClient


class MongoUtil(object):
    def __init__(self):
        pass

    def connect_mongo(self):
        # 与MongoDB建立连接，以下默认连接本地数据库，等同于
        # conn = MongoClient('localhost',27017)
        # conn = MongoClient()
        # db = conn['girl_gallery']  # 建立数据库girl_gallery
        # mzitu_collection = db['mzitu']  # 在girl_gallery数据库中创建一个集合，相当于表结构
        return MongoClient()


if __name__ == '__main__':
    conn = MongoUtil().connect_mongo()
    db = conn['girl_gallery']  # 建立数据库girl_gallery
    mzitu_collection = db['mzitu']  # 在girl_gallery数据库中创建一个集合，相当于表结构
    mzitu_collection.insert({'title': 'girl', 'url': 'xxxxxxxx'})
