#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-3-12 下午4:03
# @Author : Liuchuan
# @File   : question.py

import re


def get_answer(question):
    answer = 0
    if question is not None:
        args = re.findall("\d+", question)
        if len(args) != 2:
            return 0
        arg1,arg2 = int(args[0]),int(args[1])
        if question.find('加') != -1:
            answer = int(arg1 + arg2)
        elif question.find('减') != -1:
            answer = int(arg1 - arg2)
        elif question.find('乘') != -1:
            answer = int(arg1 * arg2)
        elif question.find('除') != -1:
            answer = int(arg1 / arg2)
    return answer
