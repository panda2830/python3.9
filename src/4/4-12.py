#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：4-12.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/2 20:16 
"""

"""
假设某游戏项目中需要定义一个精灵，其需要的属性有体重、颜色、高度、能量
具有行走、跳跃、进食能力，且会在行走和跳跃时不断损耗能量，而进食则会增加能量。
请根据描述定义这个精灵。
"""


class Elf(object):
    """
    精灵类
    有体重、颜色、高度、能量
    具有行走、跳跃、进食能力，
    且会在行走和跳跃时不断损耗能量，而进食则会增加能量。
    默认体重为10，绿色，30高度，100能量
    """

    def __init__(self, weight="10", color="green", height=30, energy=100):
        """
        构造方法
        默认体重为10，绿色，30高度，100能量
        :param weight:体重
        :param color:颜色
        :param height:高度
        :param energy:能量
        """
        self.weight = weight  # 体重
        self.color = color  # 颜色
        self.height = height  # 高度
        self.energy = energy  # 能量

    def jump(self, time):
        """
        让精灵进行跳跃多少次
        每次减少5点能量
        :param time: 次数
        :return:
        """
        for i in range(time):
            if self.energy < 5:
                print("无法跳跃能量不够，当前能量为{0}".format(self.energy))
            print("精灵正在跳跃能量-5")
            self.energy -= 5
        print("精灵剩余能量{0}".format(self.energy))

    def walk(self, time):
        """
        让精灵行走多少次
        每次减少1点能量
        :param time: 次数
        :return:
        """
        for i in range(time):
            if self.energy < 1:
                print("无法行走能量不够，当前能量为{0}".format(self.energy))
            print("精灵行走了一步能量-1")
            self.energy -= 1
        print("精灵剩余能量{0}".format(self.energy))

    def eat(self):
        """
        让精灵吃食物，能量加25
        :return:
        """
        print("精灵吃了食物能量加25")
        self.energy += 25
        print("精灵剩余能量{0}".format(self.energy))

    def __str__(self):
        return "我是一个精灵体重:{0}, 颜色:{1}, 高度{2}, 当前能量为{3}".format( \
            self.weight, self.color, self.height, self.energy)


if __name__ == "__main__":
    e1 = Elf()
    e1.jump(2)
    e1.walk(5)
    e1.eat()
    print(str(e1))
