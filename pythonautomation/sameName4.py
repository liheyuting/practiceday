#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 8:23 PM
# @Author  : Dora
# @File    : sameName4.py

def spam():
    print(eggs)
    eggs = 'spam local'

eggs = 'global'
spam()