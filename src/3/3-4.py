"""
编写一个函数，统计字符串中非字母的符号个数
"""

# ord()得到字符串的ascii值
# car()将ascii值转换回字符串
str_1 = input('输入一个字符串:')
counter = 0  # 计数器

# 遍历字符串，将单个字符转换为ASCII码，判断是否不在a-z和A-Z中
for j in iter(str_1):
    if ord(j) not in range(ord('a'), ord('z') + 1) and ord(j) not in range(ord('A'), ord('Z')):
        counter += 1
print("{0}字符串中非字母的数量为{1}".format(str_1, counter))

# for i in range(ord('a'), ord('z') + 1):
