"""
填空题
"""

"""
下面程序运行结果是()
class Coordinate():
    x = 11
    y = 11
    def __init__(self,x,y):
        self.x = x
        self.y = y

codi = Coordinate(22,22)
print(codi.x, codi.y)
"""

"""
答案：22 22
"""


class Coordinate():
    # x和y是类属性
    x = 11
    y = 11

    def __init__(self, x, y):  # 构造方法
        # 这里的x和y是构造方法的形参
        self.x = x
        self.y = y


codi = Coordinate(22, 22)
print(codi.x, codi.y)
