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
            information_1 = self.select_information(value)
            if not information_1.is_empty():
                # 方便对输入进行检查
                new_name = input(f"当前名字为{information_1.name}输入新的名字(按回车不修改):").strip()
                new_number = input(f"当前电话号码为{information_1.number}输入新的电话号码(按回车不修改):").strip()
                new_address = input(f"当前地址为{information_1.address}输入新的地址(按回车不修改):").strip()
                new_remark = input(f"当前备注为{information_1.remark}输入新的备注(按回车不修改):").strip()
                # 检查
                # if new_name == "\n":
                #     new_name = information_1.name
                # if new_number == "\n":
                #     new_number = information_1.number
                # if new_address == "\n":
                #     new_address = information_1.address
                # if new_remark == "\n":
                #     new_remark = information_1.remark
                # 写入对象
                information_1.name = new_name
                information_1.number = new_number
                information_1.address = new_address
                information_1.remark = new_remark
                print(f"现在的信息的{information_1}")
                string_1 = input("是否写入数据Y/N(默认为N):").strip()
                if string_1 in ("Y", "y", "YES", "yes"):
                    self.__open_file[value] = information_1
                    print("修改成功")
                    return True
                else:
                    print("修改取消")
                    return False
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
    # 删除数据
    # f1.delete_information("小王")
    # f1.select_information("小王")
    # 修改数据
    f1.update_information("小红")
    f1.select_information("小红")

