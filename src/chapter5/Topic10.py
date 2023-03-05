#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic10.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/5 21:33 
"""
import random
import time
from random import randint

"""
请在要执行的程序中增加计算程序运行时间的功能代码
"""

if __name__ == "__main__":
    t1 = time.time()
    for i in range(random.randint(9999999, 100000000)):
        pass
    t2 = time.time()
    print(f"运行时间为{round(t2 - t1, 3)}")
