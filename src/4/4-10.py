"""
填空题
"""

"""
下列程序运行结果的()
class A():
    x = 100
class B():
    pass
print(A.x, B.x)
"""

"""
答案：报错属性错误B类中x未定义
AttributeError
"""


class A():
    x = 100


class B():
    pass


print(A.x, B.x)
