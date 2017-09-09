#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : test02.py 
# @time  : 2017/09/06 22:48:04
# @description：to be filled
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self._event_title = []
        self._event_location = []
        self._ecent_time = []
        self._reading_title = False
        self._reading_time = False
        self._reading_location = False

    #解析头标签
    def handle_starttag(self, tag, attrs):
        if tag == 'time':
            self._reading_time = True
        if len(attrs) >= 1:
            if tag == 'h3' and attrs[0][1] == 'event-title':
                self._reading_title = True
            if tag == 'span' and attrs[0][1] == 'event-location':
                self._reading_location = True

    #解析内容
    def handle_data(self, data):
        if self._reading_title:
            self._event_title.append(data)
            self._reading_title = False
        if self._reading_time:
            self._ecent_time.append(data)
            self._reading_time = False
        if self._reading_location:
            self._event_location.append(data)
            self._reading_location = False

    @property
    def data(self):
        self._data = []
        for i in range(len(self._event_title)):
            dic = {}
            dic["title"] = self._event_title[i]
            dic["time"] = self._ecent_time[i]
            dic["location"] = self._event_location[i]
            self._data.append(dic)
        return self._data

def getHtml():
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        data = f.read().decode('utf-8')
    return data

parser = MyHTMLParser()
parser.feed(getHtml())
# for item in parser.data:
#     print(str(item))
print(parser.data[1])