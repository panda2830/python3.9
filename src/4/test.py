class Test(object):
    num_1 = 10

    def __init__(self) -> None:
        self.num2 = None

    @property
    def num_2(self):
        """返回num2"""
        return self.num2

    @num_2.getter
    def num2(self):
        print("获取了num2")
        return self.num2

    @num2.setter
    def num2(self, value):
        print("设置num2")
        self.num2 = value

    @num2.deleter
    def num2(self):
        print("删除了num2")
        del self.num2


if __name__ == "__main__":
    t2 = Test()
    print(t2.num2)
    t2.num2(123)
    del t2

