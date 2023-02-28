# numb_1 = 4
# for i in range(4+1):
#     for j in range(i+1):
#         print("{: ^16}".format('*'))

numb_1 = int(input("输入一个数值输出*号金字塔:"))
numb_2 = numb_1 + numb_1 - 1
i = 1
while i <= numb_2:
    print("{:^{}}".format('*' * i, numb_2))
    i += 2
