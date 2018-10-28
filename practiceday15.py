#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 5:13 PM
# @Author  : Dora
# @File    : practiceday15.py

#题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
n = int(input('请输入成绩\n'))


if 100>= n >= 90:
    print('A')
elif n >= 60:
    print('B')
else:
    print("C")