#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：chapter4-13.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/chapter3/chapter2 20:43
"""

"""
定义一个花的基类，包包含两个属性和至少一个方法，再定义玫瑰花和月季花两个派生类，
在派生类中对基类的方法进行改写。
最后分别创建实列对象
"""
# 导入抽象类模块
from abc import ABCMeta, abstractmethod


class Flower(object, metaclass=ABCMeta):
    """
    抽象类：花
    """

    _name: str = "flower"

    @abstractmethod
    def __init__(self, colour: str, height: int):
        """
        构造方法
        :param colour:
        :param height:
        """
        self.colour = colour
        self.height = height

    @property
    def name(self):
        return Flower._name

    @name.getter
    def name(self):
        return Flower._name

    @abstractmethod
    def display(self):
        """
        显示花的属性
        :return:
        """
        print("花的名字为{name}, 颜色为{colour}, 高度为{height}".format( \
            name=Flower._name, colour=self.colour, height=self.height))


class Rose(Flower):
    """
    玫瑰花类
    有名字，颜色和高度
    其中名字为rose且不可修改
    """
    _name = "Rose"

    def __init__(self, colour: str, height: int):
        """
        :param colour: 颜色str
        :param height: 高度int
        """
        super(Rose, self).__init__(colour, height)

    def display(self):
        super(Rose, self).display()
        pass


class Rose_Chinensis(Flower):
    """
    玫瑰花类
    有名字，颜色和高度
    其中名字为rose且不可修改
    """

    _name = "Rose_Chinensis"

    def __init__(self, colour: str, height: int):
        """
        :param colour: 颜色str
        :param height: 高度int
        """
        super(Rose_Chinensis, self).__init__(colour, height)

    def display(self):
        super(Rose_Chinensis, self).display()
        pass


if __name__ == "__main__":
    rose_1 = Rose("red", 15)
    rose_2 = Rose("red", 15)
    rose_3 = Rose("red", 15)
    rose_list = [rose_1, rose_2, rose_3]
    rose_chinensis = [x * 0 for x in range(1, 9)]

