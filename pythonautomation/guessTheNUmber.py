#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 8:42 PM
# @Author  : Dora
# @File    : guessTheNUmber.py
import random


print('I am thinking of a number bettween 1 and 20')

i = random.randint(1,21)

while True:
    a = int(input('Take a guess'))
    if a == i:
        print('Good Job! You guessed my number in 4 guesses')
        break
    elif a < i:
        print('Your guess is too low')

    elif a > i:
        print('Your guess is too high')

    else:
        print('Error')
