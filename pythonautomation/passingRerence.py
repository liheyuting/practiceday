#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 9:59 AM
# @Author  : Dora
# @File    : passingRerence.py

def eggs(someparameter):
    someparameter.append('Hello')

spam = [1,2,3]

eggs(spam)

print(spam)