"""
编程题
"""
"""
设计一个Student类,包含姓名，性别，年龄，家庭地址等属性和display()方法
在方法中将这些信息显示出来
"""


class Student(object):
    """
    学生类
    """

    def __init__(self, name: str, gender: str, age: int, home_address: str) -> None:
        """
        构造方法
        :param name: 学生的名字
        :param gender: 学生的性别
        :param age: 学生的年龄
        :param home_address: 学生的家庭住址
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.home_address = home_address

    def display(self) -> None:
        """
        输出学生的信息
        :return:
        """
        print("学生姓名:{name}, 性别{gender}, 年龄{age}, 家庭地址{home_address}".format( \
            name=self.name, gender=self.gender, age=self.age, home_address=self.home_address
        ))


if __name__ == "__main__":
    s1 = Student("xiao", "man", 18, "Beijing China")
    s1.display()