#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : parse.py 
# @time  : 2017/09/26 17:41:51
# @description：to be filled
from bs4 import BeautifulSoup
from python_spider_action.mzitu_spider.download import download
from python_spider_action.mzitu_spider.util import save


class ParseHtml(object):
    def __init__(self):
        self.download = download.DownHtml()
        self.save = save.SaveImg()

    def parse_main_page(self, base_url):
        """
        解析主页面
        :param base_url: http://www.mzitu.com/all/
        :return: 每一个a链接，比如<a href="http://www.mzitu.com/103886" target="_blank">韩国MMbebekim性感不失清新 尽显妩媚女人味!</a>
        """
        print('开始爬取主页面{}'.format(base_url))
        main_page = self.download.download_html(base_url)
        main_soup = BeautifulSoup(main_page, 'lxml')
        return main_soup.find('div', class_='all').find_all('a')

    def parse_single_page(self, url):
        """
        解析每一组页面
        :param url: 举例：http://www.mzitu.com/103886
        :return:
        """
        print('开始第一层爬取{}'.format(url))
        page = self.download.download_html(url)
        soup = BeautifulSoup(page, 'lxml')
        max_page = soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()

        for page in range(1, int(max_page) + 1):
            page_url = url + '/' + str(page)
            print('开始第二层爬取第{}页'.format(page))
            print(page_url)
            img_url = self.parse_img(page_url)
            self.save.saveImg(img_url)

    def parse_img(self, img_pre_url):
        """
        解析每一组图片的每一个页面
        :param img_pre_url: 'http://www.mzitu.com/103886/1[2|3|...]'
        :return: 图片的链接地址src: 'http://i.meizitu.net/2017/09/25b01.jpg'
        """
        img_html = self.download.download_html(img_pre_url)
        img_soup = BeautifulSoup(img_html, 'lxml')
        return img_soup.find('div', class_='main-image').find('img')['src']
