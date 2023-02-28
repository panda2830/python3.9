"""
请编程对输入的明文进行加密处理。加密方法是每个明文字母变成其后的第5个
字母，如果超过Z或z，则循环进行，即Z或z后接Aa
"""
"""
可求出
a对应97,z对应122;
A对应65,Z对应90
z对应122;Z对应90
大写和小写之间相隔32
"""
# for i in range(ord('a'), ord('z')+1):
#     print("{0}对应{1};{2}对应{3}".format(chr(i), i, chr(i-32), i-32))
# # print(chr((122 + 5) % 26 + 78))  # 小写字母加78
# # print(chr((90 + 5) % 26 + 52))  # 大写字母加52
"""
ord() 转换为ASCII码
chr() 转换为字符
"""

string_1 = input("输入字符串:")
number_1 = 5  # 向后移动的位置
string_2 = ""

for i in range(len(string_1)):
    if string_1[i].isalpha():
        # 判断是否是大写字母
        if string_1[i].isupper():
            # number_2保存轮转后字母的ASCII码
            number_2 = (ord(string_1[i]) + number_1) % 91
            if number_2 < 65:
                number_2 += 65
        else:
            number_2 = (ord(string_1[i]) + number_1) % 123
            if number_2 < 97:
                number_2 += 97
        string_2 += chr(number_2)
    else:
        string_2 += string_1[i]
print("原字符串为{0}，加密后为{1}".format(string_1, string_2))
