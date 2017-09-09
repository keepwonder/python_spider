#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : zhihu_python_title.py
# @time  : 2017/09/04 22:09:42
# @description：爬取知乎 搜索关键字Python精华的内容

from urllib import request
from html.parser import HTMLParser
import csv


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.a_title = False
        self.title = []

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag == 'a' and 'data-za-element-name' in attrs_d and 'target' in attrs_d:
            self.a_title = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.a_title = False

    def handle_data(self, data):
        if self.a_title:
            self.title.append(data)


class GetUrl(object):
    def __init__(self):
        self.url = []

    def get_all_url(self):
        for i in range(1, 51):
            url_str = 'https://www.zhihu.com/topic/19552832/top-answers?page=' + str(i)
            self.url.append(url_str)

        return self.url


class GetHtml(object):
    def __init__(self):
        self.html = []

    def get_all_html(self, urls):
        for url in urls:
            req = request.Request(url)
            req.add_header('User-Agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8')
            get_html = request.urlopen(req)
            content = get_html.read().decode('utf-8')
            self.html.append(content)

        return self.html


if __name__ == '__main__':
    gu = GetUrl()
    urls = gu.get_all_url()
    # print(gu.url)
    gh = GetHtml()
    contents = gh.get_all_html(urls)

    with open('title.csv', 'a+', encoding='utf-8') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(['Title', 'Author', 'Bio'])
        for c in contents:
            hp = MyHTMLParser()
            hp.feed(c)
            hp.close()
            for t in hp.title:
                writer.writerows([(t, '', '')])
