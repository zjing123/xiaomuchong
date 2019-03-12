#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# @TIME   :19-3-12 下午9:01
# @Author : Liuchuan
# @File   : json.py

from os import path
import json


def save_json(data, filename='./cookies.txt'):
    if not path.isdir(path.dirname(filename)):
        return False
    with open(filename, 'w') as f:
        f.truncate()
        json.dump(data, f)


def load_json(filename='./cookies.txt'):
    if not path.isfile(filename):
        return None

    if path.getsize(filename) > 0:
        with open(filename, 'r') as f:
            json_data = json.load(f)
            if json_data:
                return json_data
            else:
                return None
    else:
        return None

