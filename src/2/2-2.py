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
