#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : html_outputer.py 
# @time  : 2017/09/09 20:49:06
# @description：to be filled
import urllib.parse


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('output.html', 'w', encoding='utf-8') as f:
            f.write('<html>')
            f.write('<head><meta charset="utf-8"></head>')
            f.write('<body>')
            f.write('<table>')
            for data in self.datas:
                f.write('<tr>')
                f.write('<td>{}</td>'.format(urllib.parse.unquote(data['url'])))
                f.write('<td>{}</td>'.format(data['title']))
                f.write('<td>{}</td>'.format(data['summary']))
                f.write('</tr>')
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
