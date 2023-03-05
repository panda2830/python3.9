#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic7.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/5 20:26 
"""

import datetime

"""
请编程，分别输出当天的年份、月份、日期、星期。
"""

t = datetime.datetime.now().today()
print(f"今年是{t.year}年{t.month}月{t.day}日,是星期{t.isoweekday()}")

