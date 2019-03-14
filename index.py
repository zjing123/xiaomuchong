#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   :19-3-11 下午8:48
# @Author : Liuchuan
# @File   : index.py

# from cookies import index as login
# login_cookies = login.get_logging_cookies()
# print(login_cookies)

import requests
from lxml import etree

class Spider:
    @staticmethod
    def start_request_xiaomuchong(website):
        response = requests.get(website)
        print(response.text)
        print(response)


class Muchong(object):
    def __init__(self, start_website):
        self.website = start_website
        self.html = None

    def start_request(self):
        response = requests.get(self.website)
        print(response.text)
        self.html = response.text
        pass

    def get_atricle_links(self):
        self.start_request()
        Selector = etree.HTML(self.html)
        url_list = Selector.xpath('//td[@class="xmc_lp20"]/a/@href')
        print(url_list)



muchong_website = 'http://muchong.com/bbs/kaoyan.php?action=adjust&type=1'

xiaomuchong = Muchong(muchong_website)
xiaomuchong.get_atricle_links()
