"""
选择题
"""

"""
下列说法不正确的是()
A. 类是对象的模板，而对象是类的实例
B. python中的一切皆为对象，类本身也是对象，即类对象
C. 属性名如果以__(双下划线)开头，就变成了一个私有属性
D. 在python中一个子类只能有一个父类
"""

"""
答案：C为错误，以双下划线开头和双下划线结尾的属性为public
"""


class Test(object):
    num1 = 10  # public
    __num2 = 88  # private 只有以双下划线开头的属性为私有属性
    __num3__ = 66  # public 以双下划线开头和双下划线结尾的属性为public
    __num4_ = 33  # private


if __name__ == "__main__":
    print(Test.num1)
    # print(Test.__num2)  # 出错
    print(Test.__num3__)
    # print(Test.__num4_)  # 出错

