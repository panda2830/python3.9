"""
运算符/和运算符//的区别是什么?
答案：/为除法运算符，结果为浮点数。
//为整除运算符，两边为整数时结果为整数，一边为浮点时结果为浮点
"""

# 结果为2.59和2.0
print('除法运算符计算5.18除2的结果{0}\n整除运算符计算5.18整除2的结果{1}'.format(5.18 / 2, 5.18 // 2))

number_1 = 5.18  # 为浮点时//结果为浮点，为整数时//为整数
print(type(number_1))
print(type(number_1 / 2))
print(type(number_1 // 2))
print(type(5 // 2.1))
print(type(5 // 2))

"""
在python中%运算符可不可以对浮点数进行求余操作。
答案：在python中可以对小数进行求佘操作，但在c/c++中不行
"""
number_2 = 5.14
print(number_2 % 5)
print(number_2 % 6)
print(number_2 % 1)

"""
列表、元组、字符串是Python的有序还是无序序列？
答案：列表、元组、字符串是有序序列，其中元组字符串为不可改变的
"""

list_1 = [1, '2', 3]
tuple_1 = [4, '5', '6,7']
string_1 = "hello"

# for i, j, k in list_1, tuple_1, string_1:
#     print(i)
#     print(j)
#     print(k)

"""
什么命令既可以删除列表中的一个元素，也可以删除整个列表或其他任意类型的Python对像
答案：del

"""

list_2 = [1, 2, 3, 3]
print(list_2)
del list_2[1]
print(list_2)
del list_2
# print(list_2)  # list_2为未引用的

"""
print(32,"abc",3,sep=':')的输出结果是什么
为32:abc:3
sep是separate的缩写表示间隔
sep=':'为使用关键参数
"""
# 结果为32:abc:3
print(32, "abc", 3, sep=':')

"""
表达式9 ** (1/2)的值为
答案：为3。
9的0.5幂为根号9
结果为3，对x求0.5的幂结果是根号x的结果
"""

print("9 ** (1/2)的结果为{}".format(9 ** (1 / 2)))

"""
Python中，字典、列表、元组分别用做定界符()()()。字典的每个元素由两部分组成分别是key和value，其中key不允许重复
答案：{，[,(
key,value
key
"""

"""
假设有一个字符串 studentteacher,
 现在要求从该这符串中每隔3个字母取一个字母，则切片表达式为_______
 答案：print(string_1[::4])
 开始索引:结束索引:步长
 输出为seee
"""

string_2 = "studentteacher"
print(string_2[::4])

"""
python提供了两种实现循环的语句，分别()和()
答案：for循环为while
"""

"""
以下程序循环执行次数是___
for i in range(0,10,3):
    pass
答案为4次
从0开始到9步长为3
i=0;i<10;i+=3
"""
for i in range(0, 10, 3):
    print(i)

"""
以下是正确的Python字符串是()
A. 'abc"dd"     B. 'abc"dd'
C. 'abcc'       D. "abc\"dd\"
正确答案为C
双引号和单引用嵌套'xxx"xx"xxx'或"xxx'xx'xxx"才正确
D选项\"将转意
"""

"""
'ab'+'c'*2的结果为()
A. 'abc2'       B. 'abcabc'
C. 'abcc'       D. 'ababcc'
答案为C，*运算符优先级大于+
"""
print('ab' + 'c' * 2)

"""
以下不是python整数的是()
A. 0897     B. 0X57
C. 987      D. 0b1010
答案为A
整数不能以0开关
B选项为十六进制表示，C为十进制表示，D为二进制表示
"""

"""
以下python语句中错误的是()
A. [2,3,4][2]=5     B. (2,3,4)[2]=5
C. {'a',3,}['a']=8  C. {'a':3,}.get('b')
答案为B,元组为不可修改
C的结果为None
"""

"""
以下python表达式返回值为True的是()
A. 3 and 1 or 4     B. not 0
C. 3 < 4 > 5        D. 1 not in [1,2,3]
答案为B
and和or返回其中的值
"""
print(3 and 1 or 4)  # 返回1
print(not 0)  # 返回True
print(3 < 4 > 5)  # 返回False
print(1 not in [1, 2, 3])  # 返回False

"""
[0, 1, 2, 3][1:3]返回的值是()
A. [0,1,2,3]    B. [1,2,3]
C. [1.2]        D. [0,1,2]
答案为C，从索引1开始到3之前结束
"""
