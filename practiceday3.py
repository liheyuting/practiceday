#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 下午8:50
# @Author  : Dora
# @File    : practiceday3.py

# 题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

import math
for i in range(10000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if x * x == i+100 and y * y == i+268:
        print(i)