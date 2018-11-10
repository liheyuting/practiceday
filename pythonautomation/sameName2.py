#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 8:16 PM
# @Author  : Dora
# @File    : sameName2.py

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)