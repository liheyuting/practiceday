#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 9:28 PM
# @Author  : Dora
# @File    : bulletPointAdder.py


import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)


print(pyperclip.copy())