#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : python_org_demo.py 
# @time  : 2017/09/06 20:37:50
# @description：输出Python官网发布的会议时间、名称和地点。

from html.parser import HTMLParser
from urllib import request
import re


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.name_flag = False
        self.time_flag = False
        self.loc_flag = False
        self.name = []
        self.time = []
        self.loc = []

    def handle_starttag(self, tag, attrs):
        d_attrs = dict(attrs)
        # re_name = re.compile(r'^/events/python-events/\d+')
        # if tag == 'a' and re.match(re_name, d_attrs['href']):
        if tag == 'h3' and 'event-title' in d_attrs.values():
            self.name_flag = True
        # if tag == 'time' and 'datetime' in d_attrs:
        if tag == 'time':
            self.time_flag = True
        if tag == 'span' and 'event-location' in d_attrs.values():
            self.loc_flag = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.name_flag = False
        if tag == 'time':
            self.time_flag = False
        if tag == 'span':
            self.loc_flag = False

    def handle_data(self, data):
        if self.name_flag:
            self.name.append(data)
            self.name_flag = False
        if self.time_flag:
            self.time.append(data)
            self.time_flag = False
        if self.loc_flag:
            self.loc.append(data)
            self.loc_flag = False

    def get_result(self):
        result = []
        for i, name in enumerate(self.name):
            dict = {}
            dict['name'] = self.name[i]
            dict['time'] = self.time[i]
            dict['loc'] = self.loc[i]
            result.append(dict)
        return result


if __name__ == '__main__':
    url = 'https://www.python.org/events/python-events/'
    html = request.urlopen(url).read().decode('utf-8')
    # print(html)
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

    for item in parser.get_result():
        print(item)
