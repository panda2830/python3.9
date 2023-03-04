#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic14.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/4 8:59 
"""
"""
用面向对象的方法设计一个手机通信管理系统，
要求具有编辑、添加、删除、查询功能
"""


class Address_list(object):
    """
    通讯录类
    有姓名，手机号码，地址，备注
    """

    def __init__(self, name: str, number: int, address: str, remark: str):
        """
        构造方法
        :param name: 姓名string类型
        :param number: 电话号码int类型
        :param address: 地址string类型
        :param remark: 备注sting类型
        """
        self._remark = remark
        self._address = address
        self._number = number
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def address(self):
        return self._address

    @property
    def remark(self):
        return self._remark

    def addition(self, name: str, number: int, address: str, remark: str):
        """
        添加功能
        """
        pass

    def delete(self):
        pass

    def select(self, string_1: str):
        pass

    def redact(self):
        pass


