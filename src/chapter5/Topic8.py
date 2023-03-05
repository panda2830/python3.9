#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic8.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/5 20:38 
"""

"""
编写一个模块，定义数学中的求平方、求绝对值、判断素数3个函数，
且这个模块可以独立运行并输出一个数的平方、绝对值及是否是素数。
"""


def my_math(num: int) -> list:
    list_1 = [num ** 2]
    absolute_value = 0
    absolute_value = num if num > 0 else -num
    list_1.append(absolute_value)
    flag = False
    if num > 1:
        if num % 1 == 0:
            flag = True
            for j in range(2, num - 1):
                if num % j == 0:
                    flag = False
    list_1.append(flag)
    return list_1


if __name__ == "__main__":
    num = int(input("输入一个数:"))
    list_1 = my_math(num)
    print(list_1)