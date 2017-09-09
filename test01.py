#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : test01.py 
# @time  : 2017/09/06 22:08:45
# @description：

from html.parser import HTMLParser
from urllib import request
import re


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.time_flag = 0
        self.time = []

    def handle_starttag(self, tag, attrs):
        d_attrs = dict(attrs)
        if tag == 'time' and 'datetime' in d_attrs:
            self.time_flag = 1

    def handle_endtag(self, tag):
        if tag == 'time':
            self.time_flag = 0

    def handle_data(self, data):
        if self.time_flag:
            self.time.append(data)
            self.time_flag = 0

            # def get_result(self):
            #     result = []
            #     for i, name in enumerate(self.name):
            #         dict = {}
            #         dict['name'] = self.name[i]
            #         # dict['time'] = self.time[i]
            #         dict['loc'] = self.loc[i]
            #         result.append(dict)
            #     return result


if __name__ == '__main__':
    html = '<time datetime="2017-09-08T00:00:00+00:00">08 Sept. &ndash; 11 Sept. <span class="say-no-more"> 2017</span></time>'
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

    # for name in parser.name:
    #     print(name)
    #
    # for loc in parser.loc:
    #     print(loc)

    # for time in parser.time:
    #     print(time)

    # print(parser.get_result())
    print(parser.time)