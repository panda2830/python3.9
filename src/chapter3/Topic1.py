"""
选择题
"""
"""
有以下函数的定义，()调用会出错
def fun(outputs):
    for item in outputs:
        print(item)
A. fun([1,chapter2,chapter3])     B. fun("abcd")
C. fun(chapter3.chapter4)         D. fun((1,chapter2,chapter3))
答案为C，浮点数不可迭代
"""

def fun(outputs):
    for item in outputs:
        print(item)

# fun([1, chapter2, chapter3])
# fun("abcd")
# fun(chapter3.chapter4)
# fun((1, chapter2, chapter3))
