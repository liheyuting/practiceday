#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 10:27 PM
# @Author  : Dora
# @File    : allMyCats1.py

catNames = []

while True:
    print('Enter the name of cat '+ str(len(catNames)+ 1
                                        )+' (Or enter nothing to stop.):')

    name = input()
    if name == '':
        break
    catNames = catNames +[name]

print('The cat names are')
for name in catNames:
    print(''+name)