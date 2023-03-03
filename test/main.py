# a = [1,chapter2,chapter3]
# b = [1,chapter2,chapter3]
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# print(5//chapter2.5)
# print(eval('5//chapter2.5'))
# print("1:{1}\nchapter2:{1}\n3:{0}".format(1,chapter2))
str = "Python3.9"
# "{0:30}".format(str)
print("test01设置宽度为30默认填充空格左对齐:{0:30}\
    \ntest02设置宽度为30右对齐:{0:30}\
    \ntest03设置宽度为30居中对齐\ntest04填充*{0:*<30}\
    \ntest05填充-{0:-^30}".format(str))

num = 1234567890
print("test01:{0:-^30,}".format(num))
num = 30
print("test01十进制输出:{0:d}".format(num))
print("test01八进制输出:{0:o}".format(num))
print("test01十六进制输出:{0:x}".format(num))
print("test01二进制输出:{0:b}".format(num))
num = 3.1415926
print("test01输出浮点百分数形式:{0:%}".format(num))
print("test01输出浮点以小写e指数形式:{0:e}".format(num))
print("test01输出浮点以大写E指数形式:{0:E}".format(num))
print("test01输出浮点标准形式:{0:f}".format(num))
# !嵌套
a = "-"
b = "*"
c = "^"
d = ">"
str = "python3"
print("test01:{0:{1}{2}30}".format(str, a, c))
# !字符中类型操作符
a = "<(-)>"
print(a*3)
print("-" in a)
print("-" not in a)
b = "Python3"
c = "C/C++"
print(b+"| |"+c)
# !字符串处理方法
str = "ABCABCDDD"
print(str.center(30))
print("ABC出现的次数:{}".format(str.count("ABC")))
print("用-来分隔每个字母{}".format("-".join(str)))
