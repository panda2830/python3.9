"""
求出所有3位数水仙花数(153 = 1的3次加方5的3次方加3的3次方)
"""

for i in range(100, 1000):
    number_1 = i % 10  # 求个位
    number_2 = i % 100 // 10  # 求十位
    number_3 = i % 1000 // 100  # 求百位
    if (number_1 ** 3 + number_2 ** 3 + number_3 ** 3) == i:
        print(i)
