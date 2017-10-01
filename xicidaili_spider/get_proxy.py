#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : get_proxy.py 
# @time  : 2017/10/01 15:37:28
# @description：西刺免费代理IP爬取，并验证有效性
from bs4 import BeautifulSoup
from urllib import request
import threading
import http.client

inFile = open('proxy.txt', encoding='utf-8')
outFile = open('verified.txt', 'w', encoding='utf-8')
lock = threading.Lock()


def get_proxy_list(targeturl='http://www.xicidaili.com/nn/'):
    count_num = 0
    with open('proxy.txt', 'a', encoding='utf-8') as f:
        request_header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'}

        for page in range(1, 2):
            url = targeturl + str(page)
            # print(url)
            req = request.Request(url, headers=request_header)
            html_doc = request.urlopen(req).read()

            soup = BeautifulSoup(html_doc, 'lxml')
            trs = soup.find('table', id='ip_list').find_all('tr')

            for tr in trs[1:]:
                tds = tr.find_all('td')
                # 国家
                if tds[0].find('img') is None:
                    nation = 'unknow'
                else:
                    nation = tds[0].find('img')['alt'].strip()

                ip = tds[1].text.strip()
                port = tds[2].text.strip()
                locate = tds[3].text.strip()
                anony = tds[4].text.strip()
                protocol = tds[5].text.strip()
                speed = tds[6].find('div')['title'].strip()
                time = tds[8].text.strip()
                # 写入文件
                f.write('{}|{}|{}|{}|{}|{}|{}|{}\n'.format(nation, ip, port, locate, anony, protocol, speed, time))
                count_num += 1
    return count_num


def verify_proxy_list():
    """
    验证代理的有效性
    :return:
    """
    request_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'}
    myurl = 'https://www.baidu.com'

    while True:
        lock.acquire()
        ll = inFile.readline().strip()
        lock.release()
        if len(ll) == 0:
            break
        line = ll.strip().split('|')
        protocol = line[5]
        ip = line[1]
        port = line[2]

        try:
            conn = http.client.HTTPConnection(ip, port, timeout=1)
            conn.request(method='GET', url=myurl, headers=request_header)
            res = conn.getresponse()
            lock.acquire()
            print('+++Success:' + ip + ':' + port)
            outFile.write(ll + '\n')
            lock.release()
        except Exception as e:
            pass
            # print(e, '---Failure:' + ip + ':' + port)


if __name__ == '__main__':
    # num = get_proxy_list()
    # print(num)
    tmp = open('proxy.txt', 'w', encoding='utf-8')
    tmp.write("")
    tmp.close()

    proxy_num = get_proxy_list('http://www.xicidaili.com/nn/')
    print('国内高匿:' + str(proxy_num))
    proxy_num = get_proxy_list('http://www.xicidaili.com/nt/')
    print('国内透明:' + str(proxy_num))
    proxy_num = get_proxy_list('http://www.xicidaili.com/wn/')
    print('HTTPS代理:' + str(proxy_num))
    proxy_num = get_proxy_list('http://www.xicidaili.com/wt/')
    print('HTTP代理:' + str(proxy_num))

    print('\n验证代理的有效性:')

    all_thread = []
    for i in range(30):
        t = threading.Thread(target=verify_proxy_list)
        all_thread.append(t)
        t.start()

    for t in all_thread:
        t.join()
    inFile.close()
    outFile.close()
    print('All done.')
