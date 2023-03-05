#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic6.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/5 20:21 
"""
from calendar import calendar

"""
请编程，任意输入一个年份，即可打印全年的月历
"""


date_1 = int(input("输入年份:"))

print(calendar(date_1))
