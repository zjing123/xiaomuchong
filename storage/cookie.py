#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-12 下午5:20
# @Author : Liuchuan
# @File   : cookies.py

from storage import jsonx


def save_cookies(requests_cookie_jar, filename='./cookies.txt'):
    jsonx.save_json(requests_cookie_jar.get_dict(), filename)


def load_cookies(filename='./cookies.txt'):
    return jsonx.load_json(filename)
