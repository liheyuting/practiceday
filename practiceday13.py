#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 3:57 PM
# @Author  : Dora
# @File    : practiceday13.py

l=[]

for a in range(1,9):
    for b in range(0,9):
        for c in range(0,9):
            m = a*100 + b*10 + c
            if m == a**3 + b**3 + c**3:
                l.append(m)

print(l)

#reference answer

for n in range(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print (n)