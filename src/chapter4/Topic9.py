"""
填空题
"""

"""
下列程序运行结果是()
class Student(object):
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.scores)
stu = Student('zhangsan', 18, [88, 99, 100])
print(stu.get_name())
print(stu.get_age())
print(stu.get_course())
"""

"""
答案
zhangsan
18
100
"""


class Student(object):
    def __init__(self, name, age, scores):
        """
        test
        :param name:
        :param age:
        :param scores:
        """
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.scores)



stu = Student('zhangsan', 18, [88, 99, 100])
print(stu.get_name())
print(stu.get_age())
print(stu.get_course())
