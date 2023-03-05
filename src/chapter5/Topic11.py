#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic11.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/5 21:39 
"""
import random

"""
编写程序，生成一个包含50个随机整数的列表，然后删除其中所有的奇数
"""


def my_fun():
    list_1 = []
    for i in range(50):
        num_1 = random.randint(0, 100)
        if not (num_1 & 1):
            list_1.append(num_1)
    print(list_1)


if __name__ == "__main__":
    my_fun()
