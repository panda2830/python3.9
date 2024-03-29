#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic14.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/4 8:59 
"""
from src.chapter4.Topic14.information import information
import shelve

"""
用面向对象的方法设计一个手机通信管理系统，
要求具有编辑、添加、删除、查询功能
"""


class address_book(object):
    """
    通讯录管理系统
    具有编辑、添加、删除、查询功能
    """

    def __init__(self, value: str):
        """
        :param value: 打开的文件名称
        """
        try:
            # 打开一个持久化字典value为文件名
            self.__open_file = shelve.open(value)
            # 受保护属性_filename记录文件名
            self._file_name = value
            # test = pickle.load(self._file1)
            # key:id和value:information
        except OSError as reason:
            print(f"打开文件{value}出错" + str(reason))
        list_1 = list(self.__open_file.keys())
        print(f"已经有的记录{list_1}")

    def __del__(self):
        """
        析构函数，关闭文件
        :return:
        """
        self.__open_file.close()

    def insert_information(self, value: information) -> bool:
        """
        添加一条信息到通讯录，添加成功返回True，添加失败返回False
        :param value: 添加一个information对象到文件中
        :return:添加成功返回True，添加失败返回False
        """
        try:
            if value.name in self.__open_file:
                print(f"名字为{value.name}的信息已经有了")
                return False
            else:
                self.__open_file[value.name] = value
                print("写入文件成功")
                return True
        except IOError as reason:
            print("写入文件出错" + str(reason))

    def select_information(self, value: str) -> information:
        """
        以名字查询数据，查询成功返回information对象，失败返回空information对象
        :param value:要查询的名字
        :return:查询成功返回information对象，失败返回空information对象
        """
        information_1 = information()
        if value in self.__open_file:
            information_1 = self.__open_file[value]
            print(information_1)
            return information_1
        else:
            print(f"没有查询到这{value}")
            return information_1

    def delete_information(self, value: str) -> bool:
        """
        删除一个数据，删除成功返回True，删除失败返回False
        :param value:要删除的名字
        :return:删除成功返回True，删除失败返回False
        """
        if value in self.__open_file:
            try:
                del self.__open_file[value]
                print("删除成功")
                return True
            except KeyError as reason:
                print("索引出错" + str(reason))
        else:
            print(f"删除失败没有查询到{value}")
            return False

    def update_information(self, value: str) -> bool:
        """
        对数据进行修改，修改成功返回True，修改失败返回False
        :param value: 要修改的名字
        :return:修改成功返回True，修改失败返回False
        """
        try:
            print(f"开始对{value}进行修改")
            information_1 = self.select_information(value)
            if not information_1.is_empty():
                # 方便对输入进行检查
                new_name = input(f"当前名字为 {information_1.name} 输入新的名字(按回车不修改):").strip()
                new_number = input(f"当前电话号码为 {information_1.number} 输入新的电话号码(按回车不修改):").strip()
                new_address = input(f"当前地址为 {information_1.address} 输入新的地址(按回车不修改):").strip()
                new_remark = input(f"当前备注为 {information_1.remark} 输入新的备注(按回车不修改):").strip()
                # 检查
                if new_name in "\n":
                    new_name = information_1.name
                if new_number in "\n":
                    new_number = information_1.number
                if new_address in "\n":
                    new_address = information_1.address
                if new_remark in "\n":
                    new_remark = information_1.remark
                # 写入对象
                information_1.name = new_name
                information_1.number = new_number
                information_1.address = new_address
                information_1.remark = new_remark
                print(f"现在的信息的{information_1}")
                string_1 = input("是否写入数据Y/N(默认为N):").strip()
                if string_1 in ("Y", "y", "YES", "yes"):
                    del self.__open_file[value]
                    self.__open_file[information_1.name] = information_1
                    print("修改成功")
                    return True
                else:
                    print("修改取消")
                    return False
            else:
                print(f"没有{value}的数据")
        except IOError as reason:
            print("写入文件出错" + str(reason))


if __name__ == "__main__":
    file_1 = "test"
    f1 = address_book(file_1)
    # 添加数据
    # value1 = information("小明", 18888888888, "江西南昌", "同学")
    # value2 = information("小王", 26666666666, "江西南昌", "同学")
    # value3 = information("天天", 66688866688, "广东深圳", "老师")
    # f1.insert_information(value1)
    # f1.insert_information(value2)
    # f1.insert_information(value3)
    # 查询数据
    f1.select_information("小明")
    f1.select_information("小王")
    f1.select_information("天天")
    f1.select_information("小红")
    # 删除数据
    # f1.delete_information("小明")
    # f1.select_information("小王")
    # 修改数据
    # f1.update_information("小红")
    # f1.select_information("小明")
    # f1.select_information("大明")
    # f1.delete_information("大明")
