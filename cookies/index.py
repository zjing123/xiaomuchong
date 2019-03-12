#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# @TIME   :19-3-12 下午8:19
# @Author : Liuchuan
# @File   : index.py
import requests
from bs4 import BeautifulSoup
import time
from cookies import question
from storage import cookie
from storage import json as jsonx
from os import path

URL_BASE = 'http://muchong.com/bbs/logging.php?action=login&t='


def get_url_path(url_base='http://muchong.com/bbs/logging.php?action=login&t='):
    t = int(time.time())
    return url_base + str(t)


def load_headers(params=None):
    filename = '/configs/request/headers.json'
    filename = path.dirname(path.dirname(path.abspath(__file__))) + filename

    headers = jsonx.load_json(filename)
    if headers is not None and params is not None:
        if isinstance(params, dict):
            headers = dict(headers, **params)
    return headers


# 获取第一步登录数据：
def get_login_next1_data(url=''):
    login_next1_data = None

    response = requests.get(url=url)
    if response.status_code == 200:
        html_content = response.text

        bf = BeautifulSoup(html_content, 'html.parser')
        action = bf.find_all('form')[1].get('action')
        formhash = bf.select_one('input[name="formhash"]').get('value')
        refer = bf.select_one('input[name="refer"]').get('value')
        loginsubmit = bf.select_one('input[name="loginsubmit"]').get('value')

        login_next1_data = {
            'action': action,
            'formhash': formhash,
            'refer': refer,
            'loginsubmit': loginsubmit,
            'username': 'a8279635',
            'password': 'abc123ABC'
        }
    return login_next1_data


# 获取第二步登录数据，如：username、验证码等
def get_login_next2_data(url=''):
    login_next1_data = get_login_next1_data(url)
    if login_next1_data is None:
        return None

    headers = load_headers({'Referer': url})
    login_next2_data = None

    response = requests.post(
        url=url,
        data=login_next1_data,
        headers=headers
    )
    if response.status_code == 200:
        rbf = BeautifulSoup(response.text, 'html.parser')
        next_html = rbf.select_one('form[name="input"]')
        next_html_bf = BeautifulSoup(str(next_html), 'html.parser')

        formhash = next_html_bf.select_one('input[name="formhash"]').get('value')
        post_sec_hash = next_html_bf.select_one('input[name="post_sec_hash"]').get('value')
        username = next_html_bf.select_one('input[name="username"]').get('value')
        loginsubmit = next_html_bf.select_one('input[name="loginsubmit"]').get('value')
        ques = next_html_bf.select_one('div').text
        post_sec_code = question.get_answer(ques)

        login_next2_data = {
            'formhash': formhash,
            'post_sec_hash': post_sec_hash,
            'post_sec_code': post_sec_code,
            'username': username,
            'loginsubmit': loginsubmit
        }

    return login_next2_data


def get_logging_cookies():
    filename = './configs/cookies.txt'
    cookies = cookie.load_cookies(filename)

    if cookies is None or cookies == {}:
        url = get_url_path(URL_BASE)

        headers = load_headers({'Referer': url})
        login_next2_data = get_login_next2_data(url)

        response = requests.post(
            url,
            data=login_next2_data,
            headers=headers,
            allow_redirects=False
        )
        if response.status_code == 200 or response.status_code == 302:
            if response.cookies is not None:
                cookies = response.cookies.get_dict()
                cookie.save_cookies(response.cookies, filename)

    return cookies
