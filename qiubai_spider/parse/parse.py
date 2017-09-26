#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : parse.py 
# @time  : 2017/09/23 14:23:20
# @description：to be filled
import re


class ParseHtml(object):
    def __init__(self):
        pass

    def parse(self, content):
        # pattern = re.compile(
        #     '<div.*?author clearfix">.*?<a.*?<img.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?class="stats-.*?"class="number">(.*?)</i>')
        # pattern = re.compile('<h2>\s*(.*?)\s*</h2>\s*</a>\s*<div.*?</div>\s*</div>\s*<a.*?<div.*?class="content">\s*<span>(.*?)</span>')
        # pattern = re.compile('<div.*?class="content">\s*<span>\s*(.*?)\s*</span>')
        pattern = re.compile(
            '<h2>\s*(.*?)\s*</h2>.*?<span>(.*?)</span>.*?<span class=stats-vote><i class=number>(.*?)</i>.*?<i class=number>(.*?)</i>',
            re.S)
        items = re.findall(pattern, content)
        print(items)
        # for item in items:
        #     print(item)
            # return item[0], item[1], item[2]
