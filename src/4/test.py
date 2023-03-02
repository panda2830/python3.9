class Test(object):
    num1 = 10
    __num2 = 88  # private 只有以双下划线开头的属性为私有属性
    __num3__ = 66  # public 以双下划线开头和双下划线结尾的属性为public
    __num4_ = 33  # private


if __name__ == "__main__":
    print(Test.num1)
    # print(Test.__num2)  # 出错
    print(Test.__num3__)
    # print(Test.__num4_)  # 出错

