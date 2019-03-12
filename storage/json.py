#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# @TIME   :19-3-12 下午9:01
# @Author : Liuchuan
# @File   : json.py

import os
import json

def save_json(data, filename='./cookies.txt'):
    if not os.path.isdir(os.path.dirname(filename)):
        return False
    with open(filename, 'w') as f:
        f.truncate()
        json.dump(data, f)


def load_json(filename='./cookies.txt'):
    if not os.path.isfile(filename):
        return None

    with open(filename, 'r') as f:
        jsonData = json.load(f)
        if jsonData:
            return jsonData
        else:
            return None
