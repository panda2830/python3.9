"""
编程题
"""

"""
编写一个函数来模拟微信红包金额的分配
"""

# randbelow()方法可生成一个小于n的随机数在secrets模块
from secrets import randbelow

# print(randbelow(10))

import random

num_1 = 5  # 红包的个数
num_2 = 10  # 红包的金额


def my_fun(n1: int, n2: int) -> None:
    number_4 = num_1 - 1
    for i in range(n1):
        if i == number_4:
            print("金额为{0}".format(round(n2, 2)))
        else:
            n3 = round(random.uniform(0.1, n2), 2)
            n2 -= n3
            n1 -= 1
            print("金额为{0}".format(n3))


my_fun(num_1, num_2)
