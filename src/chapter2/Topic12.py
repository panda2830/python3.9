"""
某商品零售价为每千克8.5元，批发价为每千克6.5元
购买在10千克以上时按批发价计算。
设顾客购买文该商品为x千克，计算要付多少钱
"""

price_1 = 8.5  # 零售价为8.5元每千克
price_2 = 6.5  # 批发价为6.5元每千克

number_1 = int(input('输入购买量:'))

if number_1 > 10:
    print(price_2 * number_1)
else:
    print(price_1 * number_1)


