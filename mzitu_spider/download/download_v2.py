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

        self.iplist = ['120.78.15.63:80',
                       '183.190.47.85:80',
                       '110.73.14.137:8123',
                       '60.189.105.161:8118',
                       '61.178.238.122:63000',
                       '114.99.6.16:6890',
                       '114.223.163.122:8118',
                       '114.223.168.98:8118',
                       '112.86.70.158:80',
                       '139.224.24.26:8888',
                       '222.222.169.60:53281',
                       '101.37.79.125:3128',
                       '122.224.227.202:3128',
                       '115.154.17.122:8118',
                       '101.26.47.107:80',
                       '124.232.148.7:3128',
                       '219.135.164.245:3128',
                       '118.178.124.33:3128',
                       '122.234.178.7:811',
                       '119.5.176.36:53979',
                       '118.31.103.7:3128',
                       '183.66.64.120:3128',
                       '113.110.219.237:9999',
                       '180.97.235.30:80',
                       '182.38.193.227:8118',
                       '139.224.24.26:8888',
                       '120.78.15.63:80',
                       '118.31.103.7:3128',
                       '101.37.79.125:3128',
                       '124.232.148.7:3128',
                       '219.135.164.245:3128',
                       '122.234.178.7:8118',
                       '119.5.176.22:53979',
                       '183.66.64.120:3128',
                       '101.26.47.107:80',
                       '1.83.124.63:8118',
                       '113.227.180.82:80',
                       '117.78.37.198:8000',
                       '118.178.124.33:3128',
                       '61.135.217.7:80',
                       '119.5.176.7:4386',
                       '124.225.208.214:8118',
                       '183.45.173.238:9797',
                       '101.68.73.54:53281',
                       '114.99.6.16:6890',
                       '221.211.193.51:80',
                       '113.110.219.237:9999',
                       '111.155.116.240:8123',
                       '182.38.193.227:8118',
                       ]

    def download_html(self, url, timeout, proxy=None, num_retries=6):
        UA = random.choice(self.user_agent_list)
        headers = {'User-Agent': UA}
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
                    print(u'正在更换代理，10S后将重新获取倒数第', num_retries, u'次')
                    print(u'当前代理是：', proxy)
                    return self.download_html(url, timeout, proxy, num_retries - 1)
                else:
                    print(u'代理也不好使了！取消代理')
                    return self.download_html(url, 3)


if __name__ == '__main__':
    DownHtml().download_html('http://www.mzitu.com', 3).content
