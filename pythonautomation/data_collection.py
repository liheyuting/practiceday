#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 10:28 PM
# @Author  : Dora
# @File    : data_collection.py


import xlrd
import xlwt
import re

data1 = xlrd.open_workbook('/Users/dorali/Desktop/Python/practiceday/data collection/Marketo 05.xlsx')
data2 = xlrd.open_workbook('/Users/dorali/Desktop/Python/practiceday/data collection/Web 05.xlsx')

table1 = data1.sheets()[0]
table2 = data2.sheets()[0]

Marketo_program_name = table1.col_values(0)
Key_name = str(Marketo_program_name).splitlines()
BU = re.split('_ | - ', Key_name)

print(BU)

