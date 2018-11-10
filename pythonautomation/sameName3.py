#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 8:20 PM
# @Author  : Dora
# @File    : sameName3.py

def spam():
    global eggs
    eggs = 'spam'


def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)