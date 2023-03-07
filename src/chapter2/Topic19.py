"""
编程求解鸡兔同笼问题
设鸡免同笼，共有90只脚和30个头，
问鸡和免有多少只
暴力法

"""

foot = 90
head = 30
for i in range(100):
    for j in range(100):
        if (i * 4 + j * 2 == 90) and i + j == 30:
            print("鸡有{}只，兔有{}只".format(j, i))
