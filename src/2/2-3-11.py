"""
输入三个整数，从小到大输出
"""
list_1 = []
for i in range(3):
    list_1.append(int(input(f'输入数字{i+1}')))
print(list_1)
list_1.sort()
print(list_1)