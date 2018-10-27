#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 10:37 PM
# @Author  : Dora
# @File    : practiceday11.py

#题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

x = 1
y = 1
l =[1,1]
while x <100000:
    z = x + y
    y = x
    x = z
    l.append(z)

print(l)
