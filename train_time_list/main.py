#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : train_spider.py
# @time  : 2017/09/07 21:25:11
# @description：to be filled

# import python_spider_action.train_time_list.get_province_link as p

# if __name__ == '__main__':
    # 获取省份链接
    #     province = p.get_data().get_result()
    #     for p in province:
    #         print(p)


import python_spider_action.train_time_list.get_city_link_v2 as c
#     获取城市链接
if __name__ == '__main__':
    city = c.get_data().get_result()
    count = 0
    for c in city:
        print(c)
        count += 1
    print('共有城市数目：{}'.format(count))
