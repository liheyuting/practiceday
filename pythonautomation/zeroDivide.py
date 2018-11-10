#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 8:35 PM
# @Author  : Dora
# @File    : zeroDivide.py

def spam(divideBY):
    try:
        return 42/divideBY
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))