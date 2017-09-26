#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : makedir.py 
# @time  : 2017/09/26 20:54:55
# @description：to be filled
import os


class MakeDir(object):
    def __init__(self):
        pass

    def makedirs(self, path):
        """
        根据标题创建目录
        :param path:
        :return:
        """
        path = path.strip()
        full_path = os.path.join('/Users/jockie/Pictures/mzitu', path)
        is_exists = os.path.exists(full_path)
        if not is_exists:
            print('新建文件夹:{}'.format(path))
            os.makedirs(full_path)
            os.chdir(full_path)
            return True
        else:
            print('名字叫做{}的文件夹已经存在！！！')
