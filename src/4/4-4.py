"""
在python中，以下划线开头的变量名和方法名有特殊的含义，
尤其是在类的定义中，请仔细体会
"""

"""
以双下划线开头的属性和方法为private(私有方法)
但以双下划线开头和双下划线结尾的方法并不私有
约定用单下划线开头的属性为(protect)受保护的属性
指只读属性，不想类中的属性被外界修改
但要用@property装饰器来装饰property方法
之后就可以用setter和getter方法来方法
"""


class Test(object):
    def __init__(self, value):
        self._num1 = value

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, value):
        print("调用了num1的setter")
        self._num1 = value

    @num1.getter
    def num1(self):
        print("调用了num1的getter")
        return self._num1

    def __repr__(self):
        print("{0}类中的_num1为{1}".format(type(self), self._num1))  # 受保护的属性可被本身读取

    def __str__(self):
        return f"{self._num1}"


if __name__ == "__main__":
    t1 = Test(99)
    # print(t1._num1)  # 错误受保护的属性不可外界读写
    print(t1)
    print(t1.__repr__())
    t1.num1 = 123
    print(f"{t1.num1}")