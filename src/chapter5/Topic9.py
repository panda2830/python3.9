#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic9.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/5 21:01 
"""
import time
from random import randint

"""
请编写一个猜数游戏程序。由系统随机产生一个0-100之间的整数，玩家可以进行5次竟猜。
如果猜对了，则提示"恭喜你，猜对了！"，并结束游戏，猜错了，给玩家一个方向提示，告诉玩家是猜大了还是猜小了。
注意，可使用random模块产生随机数
"""


def guess_game() -> bool:
    print("猜随机数游戏，你有5次机会，每猜错一次都会有提示")
    num1 = randint(0, 100)
    for i in range(5):
        num2 = input("输入数值:")
        if num2.isdigit():
            num2 = int(num2)
        else:
            print("输入有错，程序结束")
            return False
        if num2 > num1:
            print("值大了")
        elif num2 < num1:
            print("值小了")
        else:
            print("恭喜你，猜对了！")
            return True
    print("次数用完，游戏结束")
    return False


if __name__ == "__main__":
    t1 = time.time()
    guess_game()
    t2 = time.time()
    print(f"运行时间为{round(t2 - t1, 3)}")
