#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 10:52 PM
# @Author  : Dora
# @File    : magic8Ball2.py

import random

message = [
    'It is certain',
    'It is decidedly so',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print(message[random.randint(0,len(message))-1])