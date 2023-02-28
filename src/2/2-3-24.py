"""
请编程对输入的明文进行加密处理。加密方法是每个明文字母变成其后的第5个
字母，如果超过Z或z，则循环进行，即Z或z后接Aa
"""
"""
可求出a对应97;A对应65
z对应122;Z对应90
大写和小写之间相隔32
"""
# for i in range(ord('a'), ord('z')+1):
#     print("{0}对应{1};{2}对应{3}".format(chr(i), i, chr(i-32), i-32))
# print(chr(122 % 122 + 97 + 4))

# string_1 = input("输入字符串:")
# string_2 = [i for i in range(len(string_1))]
# for i in string_1.__iter__():
#     i = ord(i)
#     if i in range(97, 122 + 1):
#         string_2[] = chr((i + 5) % 26)
#
# print(f"原字符串为{string_1}，加密后为{string_2}")
