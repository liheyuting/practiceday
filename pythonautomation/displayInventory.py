#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 9:36 PM
# @Author  : Dora
# @File    : displayInventory.py

Inventory = {'rope':1, 'torch':6 ,'gold coin': 42, 'dagger':1,'arrow':12}

def displayInventory(inventory):
    print("Inventory: ")
    num = 0
    for k,v in inventory.items():
        print(str(v) + ' ' +k)
        num = num + v
    print("Total number of items: " + str(num))

displayInventory(Inventory)