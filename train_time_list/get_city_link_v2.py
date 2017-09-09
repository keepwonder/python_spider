#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : get_province_link.py 
# @time  : 2017/09/07 20:28:19
# @description：全国列车时刻表在线查询,爬取城市对应链接
from html.parser import HTMLParser
from urllib import request
import re

import python_spider_action.train_time_list.get_province_link as p


class ParseCity(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.cflag = 0
        self._clink = []
        self._cname = []

    def handle_starttag(self, tag, attrs):
        clink_re = re.compile(r'^/train/[a-zA-Z]+/[a-zA-Z]+.htm$')
        # if tag == 'a' and re.match('/train/anhui/', dict(attrs)['href']):
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
        for i, cname in enumerate(self._cname):
            dict_c = {}
            dict_c['city_name'] = self._cname[i]
            dict_c['city_link'] = self._clink[i]
            result.append(dict_c)
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


class get_data(object):
    def get_result(self):
        p_urls = p.get_data().get_result()
        for p_url in p_urls:
            city_page = GetCityPage().get_page(r'http://qq.ip138.com' + p_url['province_link'])[0]
            p_parser = ParseCity()
            p_parser.feed(city_page)
            p_parser.close()
            for item in p_parser.get_result():
                yield item
                # return item

# if __name__ == '__main__':
#     p_urls = p.get_data().get_result()
#
#     for p_url in p_urls:
#         # city_page = GetCityPage().get_page(r'http://qq.ip138.com' + p_url['link'])[0]
#         # p_parser = ParseCity()
#         # p_parser.feed(city_page)
#         # p_parser.close()
#         # for item in p_parser.get_result():
#         #     print(item)
#         print(p_url)

