#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 4:28 PM
# @Author  : Dora
# @File    : practiceday14.py

#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
from math import sqrt
from  sys import stdout

m = int(input('请输入数字：\n'))

n = int(sqrt(m))
print('n = %d' %m)

for i in range(2, n+1):
    if m % i == 0:
        stdout.write(str(i))
        stdout.write("*")
        m = m/i
    else:
        break

print('%d'%m)
