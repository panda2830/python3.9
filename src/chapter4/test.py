from abc import ABCMeta, abstractmethod

"""
测试，当多继承，其中一个子类改变父类属性，另一个子类调用父类属性会不会改变
"""


class Abc_test(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, height):
        self.height = height

    @abstractmethod
    def show(self):
        print("name={0},height={1}".format(Abc_test.name, self.height))

    name = "super"

    # @abstractmethod
    # @name.setter
    # def name(self, value: str):
    #     Abc_test._name = value


class Sub1(Abc_test):
    _name = "sub1"

    @property
    def name(self):
        return Sub1._name

    # @name.setter
    # def name(self, value):
    #     Sub1._name = value

    @name.getter
    def name(self):
        return Sub1._name

    def __init__(self, height):
        super(Sub1, self).__init__(height)

    def show(self):
        print("name={0},height={1}".format(Sub1._name, self.height))
        print(Abc_test.name)


def t_fun():
    Abc_test.name = "test2"


class Sub2(Abc_test):
    _name = "sub2"

    @property
    def name(self):
        return Sub2._name

    # @name.setter
    # def name(self, value):
    #     Sub1._name = value

    @name.getter
    def name(self):
        return Sub2._name

    def __init__(self, height):
        super(Sub2, self).__init__(height)

    def show(self):
        print("name={0},height={1}".format(Sub2._name, self.height))
        print(Abc_test.name)


if __name__ == "__main__":
    sub1 = Sub1(3)
    sub1.show()
    t_fun()
    sub2 = Sub2(5)
    sub2.show()
    sub1 = Sub1(3)
    sub1.show()
