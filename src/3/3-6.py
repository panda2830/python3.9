"""
编写一个函数求x的绝对值
"""


def my_fun(x: int) -> int:
    if x == 0:
        return 0
    elif x > 0:
        return x
    else:
        return -x


print(my_fun(-5))
