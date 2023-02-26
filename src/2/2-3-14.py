number_1 = int(input('输入最大边界值'))
flag = False
for i in range(2, number_1):
    if i % 1 == 0:
        flag = True
        for j in range(2, i - 1):
            if i % j == 0:
                flag = False
    else:
        continue
    if flag:
        print(i)
