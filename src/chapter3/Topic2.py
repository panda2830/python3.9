"""
选择题
"""
"""
对于以下代码，输出结果依次是()
a = chapter3
b = [1,chapter2]
def fun(a,b):
    #定义一个局部变量a
    a = 9
    b.append(chapter3)
    print(a, b)
fun(a, b)
print(a, b)
A. chapter3[1,chapter2]chapter3[1,chapter2]     B. 9[1,chapter2,chapter3]chapter3[1,chapter2,chapter3]
C. 9[1,chapter2,chapter3]9[1,chapter2,chapter3] D. chapter3[1,chapter2,chapter3]9[1,chapter2,chapter3]
答案：B
参数为可变序列引用传递时，可以改变序列中元素的值，可通过id
"""
a = 3
b = [1, 2]
print("函数执行前")
print("a的地址为:{0}\nb的地址为:{1}".format(id(a), id(b)))


def fun(a, b):
    # 定义一个局部变量a
    a = 9
    print("函数执行中")
    print("a的地址为:{0}\nb的地址为:{1}".format(id(a), id(b)))
    b.append(3)
    print(a, b)


fun(a, b)
print(a, b)

print("函数执行后")
print("a的地址为:{0}\nb的地址为:{1}".format(id(a), id(b)))
