"""
请编写程序计算任意输入的20个数中正数、负数、0的个数
"""
my_list = list()
number_1 = 0  # 正数
number_2 = 0  # 负数
number_3 = 0  # 0
for i in range(20):
    # my_list.append(int(input("输入20个数:{i}/20: ")))
    number_4 = int(input(f"输入20个数:{i+1}/20: "))
    if number_4 < 0:
        number_2 += 1
    elif number_4 > 0:
        number_1 += 1
    else:
        number_3 += 1
print("正数有{0}个，负数有{1}个，0有{2}个".format(number_1, number_2, number_3))