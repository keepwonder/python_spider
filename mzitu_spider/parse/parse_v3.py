#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : parse.py 
# @time  : 2017/09/26 17:41:51
# @description：to be filled
from bs4 import BeautifulSoup
from python_spider_action.mzitu_spider.download import download_v3
from python_spider_action.mzitu_spider.util import save_v3
from python_spider_action.mzitu_spider.util import mongoUtil, makedir
import datetime


class ParseHtml(object):
    def __init__(self):
        self.download = download_v3.DownHtml()
        self.mkdir = makedir.MakeDir()
        self.save = save_v3.SaveImg()
        self.dbclient = mongoUtil.MongoUtil().connect_mongo()  # 连接本地MongoDB
        self.picdb = self.dbclient['girl_gallery']  # 建立girl_gallery数据库
        self.picset = self.picdb['girl_pic']  # 建立girl_pic集合(相关于表结构)
        self.title = ''  # 保存页面主题
        self.url = ''  # 保存页面地址
        self.img_urls = []  # 初始化一个列表，用来保存图片地址

    def parse_main_page(self, base_url):
        """
        解析主页面
        :param base_url: http://www.mzitu.com/all/
        :return: 每一个a链接，比如<a href="http://www.mzitu.com/103886" target="_blank">韩国MMbebekim性感不失清新 尽显妩媚女人味!</a>
        """
        print('开始爬取主页面{}'.format(base_url))
        main_page = self.download.download_html(base_url, 3)
        main_soup = BeautifulSoup(main_page.text, 'lxml')
        all_a = main_soup.find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            self.title = title  # 将主题保存到self.title中
            print('开始保存：{}'.format(title))
            path = str(title)
            self.mkdir.makedirs(path)
            href = a['href']
            self.url = href  # 将页面地址保存到self.url中
            if self.picset.find_one({'主题页面': href}):
                print('该页面已经爬取过')
            else:
                self.parse_single_page(href)

    def parse_single_page(self, url):
        """
        解析每一组页面
        :param url: 举例：http://www.mzitu.com/103886
        :return:
        """
        print('开始第一层爬取{}'.format(url))
        page = self.download.download_html(url, 3)
        soup = BeautifulSoup(page.text, 'lxml')
        max_page = soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
        page_num = 0  #这个当作计数器用 （用来判断图片是否下载完毕）

        for page in range(1, int(max_page) + 1):
            page_num += 1  # 每for循环一次就+1  （当page_num等于max_span的时候，就证明我们的在下载最后一张图片了）
            page_url = url + '/' + str(page)
            print('开始第二层爬取第{}页'.format(page))
            print(page_url)
            self.parse_img(page_url, max_page, page_num)

    def parse_img(self, img_pre_url, max_page, page_num):
        """
        解析每一组图片的每一个页面
        :param img_pre_url: 'http://www.mzitu.com/103886/1[2|3|...]'
        :return: 图片的链接地址src: 'http://i.meizitu.net/2017/09/25b01.jpg'
        """
        img_html = self.download.download_html(img_pre_url, 3)
        img_soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_soup.find('div', class_='main-image').find('img')['src']
        self.img_urls.append(img_url)
        if int(max_page) == page_num:
            self.save.saveImg(img_url)
            post = {  # 这是构造一个字典，里面有啥都是中文，很好理解吧！
                '标题': self.title,
                '主题页面': self.url,
                '图片地址': self.img_urls,
                '获取时间': datetime.datetime.now()
            }
            self.picset.save(post)  # 将post中的内容写入数据库。
            print(u'插入数据库成功')
        else:
            self.save.saveImg(img_url)
