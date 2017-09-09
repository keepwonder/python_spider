#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : get_province_link.py 
# @time  : 2017/09/07 20:28:19
# @description：全国列车时刻表在线查询,爬取省份对应链接

from html.parser import HTMLParser
from urllib import request
import re


class ParseProvince(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.pflag = 0
        self._plink = []
        self._pname = []

    def handle_starttag(self, tag, attrs):
        plink_re = re.compile(r'^/train/[a-zA-Z]+/')
        # if tag == 'a' and re.match('/train/anhui/', dict(attrs)['href']):
        if tag == 'a' and len(attrs) == 1 and re.match(plink_re, attrs[0][1]):
            for name, value in attrs:
                self._plink.append(value)
            self.pflag = 1

    def handle_data(self, data):
        if self.pflag:
            self._pname.append(data)
            self.pflag = 0

    def handle_endtag(self, tag):
        if tag == 'a':
            self.pflag = 0

    def get_result(self):
        result = []
        for i, pname in enumerate(self._pname):
            dict_p = {}
            dict_p['province_name'] = self._pname[i]
            dict_p['province_link'] = self._plink[i]
            result.append(dict_p)
        return result


class GetProvincePage(object):
    def __init__(self):
        self.page = []

    def get_page(self, url):
        req = request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8')
        get_html = request.urlopen(req)
        content = get_html.read().decode('gb2312')
        self.page.append(content)
        return self.page


# if __name__ == '__main__':
#     start_url = 'http://qq.ip138.com/train/'
#     html = GetProvincePage().get_page(start_url)[0]
#     p_parser = ParseProvince()
#     p_parser.feed(html)
#     p_parser.close()
#
#     for item in p_parser.get_result():
#         print(item)

class get_data(object):
    def get_result(self):
        start_url = 'http://qq.ip138.com/train/'
        html = GetProvincePage().get_page(start_url)[0]
        p_parser = ParseProvince()
        p_parser.feed(html)
        p_parser.close()

        for item in p_parser.get_result():
            yield item
        # return item
