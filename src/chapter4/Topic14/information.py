#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：information.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/5 13:50 
"""


class information(object):
    """
    信息类
    有姓名，手机号码，地址，备注
    """

    def __init__(self, name: str = "null", number: int = None, address: str = "null", remark: str = "null"):
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
        """name为受保护的"""
        return self._name

    @name.getter
    def name(self) -> str:
        """获取name方法"""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """设置name新值方法"""
        self._name = value

    @property
    def number(self):
        """number为受保护的"""
        return self._number

    @number.getter
    def number(self) -> int:
        """获取number方法"""
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        """设置number新值方法"""
        self._number = value

    @property
    def address(self):
        """address为受保护的"""
        return self._address

    @address.getter
    def address(self) -> str:
        """获取address方法"""
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        """设置address新值方法"""
        self._address = value

    @property
    def remark(self):
        """remark为受保护的"""
        return self._remark

    @remark.getter
    def remark(self) -> str:
        """获取remark方法"""
        return self._remark

    @remark.setter
    def remark(self, value: str) -> None:
        """设置remark新值方法"""
        self._remark = value

    def __str__(self):
        return f"名字:{self._name}\t电话号码:{self._number}\t地址:{self._address}\t备注:{self._remark}"

    def is_empty(self) -> bool:
        """判断是否为空"""
        if self._name == 'null' or self._number is None:
            return True
        else:
            return False
