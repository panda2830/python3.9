# numb_1 = chapter4
# for i in range(chapter4+1):
#     for j in range(i+1):
#         print("{: ^16}".format('*'))

num_1 = int(input("输入一个数值输出*号金字塔:"))
num_2 = num_1 + num_1 - 1
i = 1
while i <= num_2:
    print("{:^{}}".format('*' * i, num_2))
    i += 2

