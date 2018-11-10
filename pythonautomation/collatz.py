#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 9:16 PM
# @Author  : Dora
# @File    : collatz.py

intName = int(input('Please enter a number'))


def collatz(i):
    if i == 1:
        break
    print('1')

    if i>1 & i % 2 == 0:
        i = i / 2
        print(i)
        return collatz()
    elif i>1 & i % 2 != 2:
        i = 3 * i + 1
        print(i)
        return collatz()
    else:
        print('Error')


while True:
    collatz(intName)





