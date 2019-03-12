#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   :19-3-11 下午8:48
# @Author : Liuchuan
# @File   : index.py

import requests
from bs4 import BeautifulSoup
import time
import cookies.question as question
from storage import cookie


def get_url_path(url_base='http://muchong.com/bbs/logging.php?action=login&t='):
    t = int(time.time())
    return url_base + str(t)


url_base = 'http://muchong.com/bbs/logging.php?action=login&t='
url_path = get_url_path()

req = requests.get(url=url_path)
htmlContent = req.text

bf = BeautifulSoup(htmlContent, 'html.parser')

action = bf.find_all('form')[1].get('action')
formhash = bf.select_one('input[name="formhash"]').get('value')
refer = bf.select_one('input[name="refer"]').get('value')
loginSubmit = bf.select_one('input[name="loginsubmit"]').get('value');

userAgent = r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
headers= {
    'Host': 'muchong.com',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control' : 'max-age=0',
    'User-Agent': userAgent,
    'Proxy-Connection': 'Keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests' : '1',
    'Referer': url_path,
    'Cookie' : '_ga=GA1.2.1884146983.1552061558; _discuz_cc=88551566024268178; _emuch_index=1; _gat=1'
}

# proxies = {'http': 'http://127.0.0.1:44075', 'https': 'http://127.0.0.1:44075'}

loginData = {
    'formhash': formhash,
    'username': 'a8279635',
    'password': 'abc123ABC',
    'cookietime': 31536000,
    'loginsubmit': loginSubmit,
    'refer': refer
}

res = requests.post('http://muchong.com/bbs/' + action, data=loginData, headers=headers)
if res.status_code == 200:
    rbf = BeautifulSoup(res.text, 'html.parser')
    NextHtml = rbf.select_one('form[name="input"]')
    nexthtmlBF = BeautifulSoup(str(NextHtml), 'html.parser')

    formhash = nexthtmlBF.select_one('input[name="formhash"]').get('value')
    post_sec_hash = nexthtmlBF.select_one('input[name="post_sec_hash"]').get('value')
    username = nexthtmlBF.select_one('input[name="username"]').get('value')
    loginsubmit = nexthtmlBF.select_one('input[name="loginsubmit"]').get('value')

    ques = nexthtmlBF.select_one('div').text
    post_sec_code = question.get_answer(ques)
    # print(question)
    # print(post_sec_code)
    # print(NextHtml)

    loginData = {
        'formhash': formhash,
        'post_sec_hash': post_sec_hash,
        'post_sec_code': post_sec_code,
        'username': username,
        'loginsubmit': loginsubmit
    }

    html = requests.post(url_path, data=loginData, headers=headers, allow_redirects=False)
    if html.status_code == 200 or html.status_code == 302:
        cookie.save_cookies(html.cookies, './configs/cookies.txt')
