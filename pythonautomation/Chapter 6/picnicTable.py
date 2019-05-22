#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 3:33 PM
# @Author  : Dora
# @File    : picnicTable.py

def printPicnic(itemsDict, leftWidth, rightwidth):
    print('Print items'.center(leftWidth + rightwidth,'-') )
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightwidth))

picnicItems = {'sandwiches': 4, 'apple': 12, 'cups':4, 'cookies': 8000}
printPicnic(picnicItems, 12,5 )
printPicnic(picnicItems, 20, 6)