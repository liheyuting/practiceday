#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 下午10:59
# @Author  : Dora
# @File    : practiceday5.py

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。


# 自己琢磨，成功
# x = int(input())
# y = int(input())
# z = int(input())
#
# if x <= y:
#     if y <= z:
#         print(x,y,z)
#     elif z <=x:
#         print(z,x,y)
#     else:
#         print(x,z,y)
# else:
#     if y >= z:
#         print(z,y,x)
#     elif x >= z >y :
#         print(y,z,x)
#     else:
#         print(y,x,z)
#


# 参考答案，简洁，使用了dict/append/sort
l = []

for i in range(3):
    i = int(input())
    l.append(i)

l.sort()
print(l)
