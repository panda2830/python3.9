"""
类对象和实例对象的区别是什么
"""

"""
python中的类对象和实例对象也是python中的对象，
定义类后可以当前作用域中生成一个以类名的类
可以通过 类名() 的方式实例化一个对象
可以通过 类名.类属性 的方式来访问一个类属性
类是抽象的，实例对象是具体的
类相当于蓝图，实例对象相当于按蓝图构造出来的物品
"""


# 继承object类是新式类，区别于基本类继承搜索函数为深度优先搜索。而新类为广度优先搜索
class Test(object):
    num1 = 10

    def __init__(self):
        self.num2 = 5

