#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 6:58 PM
# @Author  : Dora
# @File    : 2.py


#2.2

import pygame, sys

from pygame.locals import  *

pygame.init()
displaysurf = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello, world')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()