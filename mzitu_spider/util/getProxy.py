#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : getProxy.py
# @time  : 2017/09/26 22:08:01
# @description：to be filled
import urllib.request
from bs4 import BeautifulSoup


class GetProxy(object):
    def __init__(self):
        self.ip_set = set()

    def getIP(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
            'Referer': 'http://www.kuaidaili.com/free/inha/'
        }
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response, 'lxml')
        all_tr = soup.find('div', attrs={'id': 'footer', 'class': 'footer'}).find_all('td')[5:]
        for i in range(0, len(all_tr), 5):
            ip = str(all_tr[i].get_text()) + ':' + str(all_tr[i + 1].get_text())
            self.ip_set.add(ip)
            for ip in self.ip_set:
                with open('ip.txt', 'a') as f:
                    f.writelines(str(ip))
                    # return self.ip_set
        # print(self.ip_set)
        for ip in self.ip_set:
            print(ip)

if __name__ == '__main__':
    # GetProxy().getIP('http://www.kuaidaili.com/free/inha/') # urllib.error.HTTPError: HTTP Error 521:
    for i in range(1, 3):
        for j in range(1, 3):
            GetProxy().getIP(
                'http://www.66ip.cn/areaindex_{}/{}.html'.format(i, j))