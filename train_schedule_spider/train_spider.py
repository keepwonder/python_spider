#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : train_spider.py
# @time  : 2017/09/23 23:52:32
# @description：to be filled
import urllib.parse
import requests
import csv
import os
import multiprocessing as mp

from bs4 import BeautifulSoup

ROOT_URL = 'http://qq.ip138.com/train/'
PROVINCE_LINK = {}
CITY_LINK = {}
TRAIN_INFO = []


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None


def parse_province_page(html):
    soup = BeautifulSoup(html, 'lxml')
    all_a = soup.find_all('table', attrs={'width': 600})[1].find_all('a')
    for a in all_a:
        # print(a['href'], '-------', a.string)
        PROVINCE_LINK[a.string] = urllib.parse.urljoin(ROOT_URL, a['href'])

    return PROVINCE_LINK


def parse_city_page(html):
    soup = BeautifulSoup(html, 'lxml')
    all_a = soup.find('table', attrs={'width': 420}).find_all('a')
    for a in all_a:
        # print(a.string, '-----', a['href'])
        CITY_LINK[a.string] = urllib.parse.urljoin(ROOT_URL, a['href'])

    return CITY_LINK


def parse_train_timetable(html, filename):
    soup = BeautifulSoup(html, 'lxml')
    checilist = soup.find('div', attrs={'id': 'checilist'})
    # print(checilist)
    if checilist:
        all_td = checilist.find_all('td')
        all_td_list = list(all_td)
        file = filename + '.csv'
        path = os.path.join('csv/', file)
        with open(path, 'w', encoding='utf-8') as csvfile:
            print('开始写入: ', filename)
            writer = csv.writer(csvfile)
            writer.writerow(['车次', '列车类型', '始发站', '始发时间', '经过站', '经过站到达时间', '经过站发车时间', '终点站', '到达时间'])
            for i in range(0, len(all_td_list), 9):
                train_list = [all_td_list[i].string,
                              all_td_list[i + 1].string,
                              all_td_list[i + 2].string,
                              all_td_list[i + 3].string,
                              all_td_list[i + 4].string,
                              all_td_list[i + 5].string,
                              all_td_list[i + 6].string,
                              all_td_list[i + 7].string,
                              all_td_list[i + 8].string, ]
                # TRAIN_INFO.append(train_list)
                writer.writerows([train_list])
                # print(TRAIN_INFO)
                # return TRAIN_INFO


def main():
    province_html = get_page(ROOT_URL)
    province_links = parse_province_page(province_html)
    # print(province_links.values())
    for p_link in province_links.values():
        print(p_link)
        city_html = get_page(p_link)
        city_links = parse_city_page(city_html)

    for c_link in city_links.values():
        # with open('city_link.txt', 'a', encoding='utf-8') as f:
        #     f.write(c_link + '\n')
        filename = c_link.split('/')[-1][:-4]
        # train_list = get_page('http://qq.ip138.com/train/chongqing/huanglian.htm')
        train_list = get_page(c_link)
        parse_train_timetable(train_list, filename)


if __name__ == '__main__':
    p = mp.Pool()
    for i in range(mp.cpu_count()):
        p.apply_async(main)
    p.close()
    p.join()
