# ord()得到字符串的ascii值
# car()将ascii值转换回字符串
str_1 = input('输入一个字符串:')
counter = 0

for j in iter(str_1):
    if ord(j) not in range(ord('a'), ord('z') + 1):
        counter += 1
print("{0}字符串中非字母的数量为{1}".format(str_1, counter))

# for i in range(ord('a'), ord('z') + 1):
