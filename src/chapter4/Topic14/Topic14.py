#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic14.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/4 8:59 
"""
import shelve

"""
用面向对象的方法设计一个手机通信管理系统，
要求具有编辑、添加、删除、查询功能
"""

import pickle


class information(object):
    """
    信息类
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

    @name.getter
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def number(self):
        return self._number

    @number.getter
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        self._number = value

    @property
    def address(self):
        return self._address

    @address.getter
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = value

    @property
    def remark(self):
        return self._remark

    @remark.getter
    def remark(self) -> str:
        return self._remark

    @remark.setter
    def remark(self, value: str) -> None:
        self._remark = value

    def __str__(self):
        return f"名字:{self._name}\t电话号码:{self._number}\t地址:{self._address}\t备注:{self._remark}"


class address_book(object):
    """
    通讯录管理系统
    具有编辑、添加、删除、查询功能
    """

    def __init__(self, value: str):
        """
        构造方法，接收一个字符串作为要打开文件的名称类型string
        :param value:
        """
        # self.open_file = shelve.open(value)
        try:
            self.open_file = shelve.open(value)
            self._filename = value
            # test = pickle.load(self._file1)
            # key:id和value:information
            self.information_dict = {}
        except OSError as reason:
            print(f"打开文件{value}出错" + str(reason))

    def add_information(self, value: information):
        """
        添加一条信息到通讯录
        :type value: object
        :param value: 添加一个information对象到文件中
        :return:
        """
        # 向字典内添加一个information对象
        self.information_dict[value.name] = value
        try:
            self.open_file[value.name] = value
        except IOError as reason:
            print("写入文件出错" + str(reason))
        print("写入文件成功")

    def select_information(self, value: str):
        if value in self.open_file:
            in1 = self.open_file[value]
            print(in1)
        else:
            print("没有这个人")

    def delete_information(self, value: str):
        if value in self.open_file:
            try:
                del self.open_file[value]
            except KeyError as reason:
                print("索引出错" + str(reason))
        else:
            print("删除失败没有这个人")


if __name__ == "__main__":
    file_1 = "test"
    f1 = address_book(file_1)
    value1 = information("小明", 18888888888, "江西南昌", "同学")
    value2 = information("小王", 26666666666, "江西南昌", "同学")
    value3 = information("天天", 66688866688, "广东深圳", "老师")
    # f1.add_information(value1)
    # f1.add_information(value2)
    # f1.add_information(value3)
    f1.select_information("小明")
    f1.select_information("小王")
    f1.select_information("天天")
    # f1.delete_information("小王")
    # f1.select_information("小王")
