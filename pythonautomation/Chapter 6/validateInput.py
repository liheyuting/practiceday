#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 7:07 AM
# @Author  : Dora
# @File    : validateInput.py


while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Plese enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only)')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')


#第一个while循环，age是有效的值（数字），就跳出第一个循环
#第二个while循环，客户的输入保存在password肿，如果输入的是字母或是数字，就跳出循环，否则要求再次输入