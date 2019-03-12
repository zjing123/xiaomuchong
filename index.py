#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   :19-3-11 下午8:48
# @Author : Liuchuan
# @File   : index.py

from cookies import index as login

login_cookies = login.get_logging_cookies()

print(login_cookies)


