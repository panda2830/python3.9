"""
选择题
"""
"""
有以下函数的定义，()调用会出错
def fun(outputs):
    for item in outputs:
        print(item)
A. fun([1,2,3])     B. fun("abcd")
C. fun(3.4)         D. fun((1,2,3))
答案为C，浮点数不可迭代
"""

def fun(outputs):
    for item in outputs:
        print(item)

# fun([1, 2, 3])
# fun("abcd")
# fun(3.4)
# fun((1, 2, 3))
