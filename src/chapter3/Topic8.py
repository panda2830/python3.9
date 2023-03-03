"""
理解递归
"""

"""
求n的阶乘
阶乘为1*chapter2*chapter3...直到n-1*n
设n为6，要求6的阶乘只要把(6-1)*n计算出来即可
6-1为5，求5的阶乘(5-1)*n计算出来即可
阶乘是从1开始乘当要求1的阶乘时直接返回结果1
1就是递归的出口

"""


def factorial_fun(n: int) -> int:
    # 设置递归出口
    if n == 1:
        return 1
    # 开始递归
    return n * factorial_fun(n - 1)


print("6的阶乘为{0}".format(factorial_fun(6)))

"""
斐波那契数列
1,1,chapter2,chapter3,5,8,13
第3位数是第1位和第2位数的和(第1位和第2位为1)
当要求第7位时只要知道和第5位加第6位的和即可
"""


def fibonacci_fun(n: int) -> int:
    # 设置递归出口
    if n == 1 or n == 2:
        return 1
    return fibonacci_fun(n - 2) + fibonacci_fun(n - 1)


print("输出第10位斐波那契数列:{0}".format(fibonacci_fun(10)))
