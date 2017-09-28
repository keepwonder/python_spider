#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : download_v2.py 
# @time  : 2017/09/26 21:57:33
# @description：to be filled

import requests
import random
import time


class DownHtml(object):
    def __init__(self):
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"
        ]

        self.iplist = ['211.159.171.58:80',
                       '101.129.17.33:808',
                       '111.231.13.171:80',
                       '123.115.165.153:9',
                       '120.78.15.63:80',
                       '43.241.10.206:808',
                       '118.31.103.7:3128',
                       '122.49.35.168:331',
                       '111.155.116.237:8',
                       '59.66.199.15:8123',
                       '211.154.196.238:3',
                       '119.90.63.3:3128',
                       '124.127.105.236:8',
                       '122.72.32.88:80',
                       '122.72.32.98:80',
                       '111.13.135.172:80',
                       '111.13.7.123:80',
                       '120.132.71.212:80',
                       '182.61.13.16:3128',
                       '111.206.186.40:80',
                       '117.78.35.194:312',
                       '182.61.58.100:312',
                       '111.13.7.122:80',
                       '111.13.61.59:3128',
                       '221.179.253.42:81',
                       '111.13.2.138:80',
                       '162.105.28.232:99',
                       '103.233.157.236:5',
                       '122.72.32.72:80',
                       '116.224.191.202:8',
                       '114.89.157.106:81',
                       '101.224.213.137:9',
                       '202.121.178.244:8',
                       '116.236.151.166:8',
                       '114.89.203.81:532',
                       '180.173.121.150:9',
                       '202.120.1.32:80',
                       '180.168.217.14:90',
                       '116.231.182.233:5',
                       '114.80.143.140:80',
                       '180.164.206.80:90',
                       '218.193.183.9:812',
                       '222.66.22.82:8090',
                       '180.170.63.64:811',
                       '116.226.71.214:90',
                       '116.224.207.183:9',
                       '180.173.54.155:90',
                       '124.78.212.43:900',
                       '58.247.127.145:53',
                       '116.231.148.33:53',
                       '180.173.48.187:53',
                       '120.204.85.29:312',
                       '222.73.68.144:809']

    def download_html(self, url, timeout, proxy=None, num_retries=6):
        UA = random.choice(self.user_agent_list)
        referer = 'http://www.mzitu.com/'
        headers = {'User-Agent': UA, 'Referer': referer}
        if proxy == None:
            try:
                response = requests.get(url, headers=headers, timeout=timeout)
                return response
            except:
                if num_retries > 0:  # 限定重试次数
                    time.sleep(5)  # 延迟5秒
                    print('获取页面出错，5s后重试倒数第{}次'.format(num_retries))
                    return self.download_html(url, timeout, num_retries - 1)
                else:
                    print('开始使用代理')
                    time.sleep(5)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': IP}
                    return self.download_html(url, timeout, proxy)
        else:
            try:
                IP = ''.join(str(random.choice(self.iplist)).strip())
                proxy = {'http': IP}
                response = requests.get(url, headers=headers, proxy=proxy, timeout=timeout)
                return response
            except:
                if num_retries > 0:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': IP}
                    print('正在更换代理，10S后将重新获取倒数第', num_retries, '次')
                    print('当前代理是：', proxy)
                    return self.download_html(url, timeout, proxy, num_retries - 1)
                else:
                    print('代理也不好使了！取消代理')
                    return self.download_html(url, 3)


if __name__ == '__main__':
    a = DownHtml().download_html('http://www.mzitu.com', 3).content
    print(a.decode('utf-8'))
