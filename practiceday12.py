#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 10:44 PM
# @Author  : Dora
# @File    : practiceday12.py

#题目：判断101-200之间有多少个素数，并输出所有素数。

from math import sqrt

l = []

for i in range(101,200):
    n = int(sqrt(i+1))
    leap = 1

    for x in range(2, n+1):
        if i % x == 0:
            leap = 0
    if leap == 1:
            l.append(i)


print(l,'Tatol is %d'%len(l))

# 参考答案

h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d' % m)
        h += 1
        if h % 10 == 0:
            print ('')
    leap = 1
print ('The total is %d' % h)