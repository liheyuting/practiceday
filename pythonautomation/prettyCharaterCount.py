#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 7:12 AM
# @Author  : Dora
# @File    : characterCount.py
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

pprint.pprint(count)