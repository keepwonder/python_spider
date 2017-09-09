#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : get_province_link.py 
# @time  : 2017/09/07 20:28:19
# @description：全国列车时刻表在线查询,爬取城市对应链接

from html.parser import HTMLParser
from urllib import request
import re

import python_spider_action.train_time_list.get_province_link as plink


class ParseCity(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.cflag = 0
        self._clink = []
        self._cname = []

    def handle_starttag(self, tag, attrs):
        clink_re = re.compile(r'^/train/[a-zA-Z]+/[a-zA-Z].htm$')
        if tag == 'a' and len(attrs) == 1 and re.match(clink_re, attrs[0][1]):
            for name, value in attrs:
                self._clink.append(value)
            self.cflag = 1

    def handle_data(self, data):
        if self.cflag:
            self._cname.append(data)
            self.cflag = 0

    def handle_endtag(self, tag):
        if tag == 'a':
            self.cflag = 0

    def get_result(self):
        result = []
        for i, pname in enumerate(self._cname):
            dict_p = {}
            dict_p['name'] = self._cname[i]
            dict_p['link'] = self._clink[i]
            result.append(dict_p)
        return result


class GetCityPage(object):
    def __init__(self):
        self.page = []

    def get_page(self, url):
        req = request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8')
        get_html = request.urlopen(req)
        content = get_html.read().decode('gb2312', 'ignore')
        self.page.append(content)
        return self.page


class GetCityLink(object):
    def get_data(self):
        urls = plink.get_data().get_result()
        for url in urls:
            # city_page = GetCityPage().get_page(r'http://qq.ip138.com'+url['link'])[0]
            # pcity = ParseCity()
            # pcity.feed(city_page)
            # pcity.close()
            # for item in pcity.get_result():
            #     yield item
            yield url