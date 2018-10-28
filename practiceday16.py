#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 5:21 PM
# @Author  : Dora
# @File    : practiceday16.py

#题目：输出指定格式的日期
import time

a = time.asctime(time.localtime(time.time()))
b = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(a,b)