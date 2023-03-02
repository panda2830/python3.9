#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：4-13.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/2 20:43 
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

    @abstractmethod
    def __init__(self, colour: str, height: int):
        """
        构造方法
        :param colour:
        :param height:
        """
        self.colour = colour
        self.height = height

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
    """

    def __init__(self, colour: str, height: int):
        super(Rose, self).__init__(colour, height)
        Flower.name = "玫瑰花"

    def display(self):
        super(Rose, self).display(self)
        pass
