#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 10:36 PM
# @Author  : Dora
# @File    : myPets.py

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named' +name)
else:
    print(name + ' is my pet.')
