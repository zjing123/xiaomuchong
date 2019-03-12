#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# @TIME   :19-3-12 下午9:12
# @Author : Liuchuan
# @File   : test.py

from storage import jsonx

header = jsonx.load_json('./configs/request/headers.json')
print(type(header))
