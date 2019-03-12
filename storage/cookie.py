#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-12 下午5:20
# @Author : Liuchuan
# @File   : cookies.py

from storage import json as jsonx

def save_cookies(RequestsCookieJar, filename='./cookies.txt'):
    jsonx.save_json(RequestsCookieJar.get_dict(), filename)


def load_cookies(filename='./cookies.txt'):
    return jsonx.load_json(filename)
