#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 8:12 PM
# @Author  : Dora
# @File    : sameName.py

def span():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    span()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)