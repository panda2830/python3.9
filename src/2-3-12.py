price_1 = 8.5  # 零售价为8.5元每千克
price_2 = 6.5  # 批发价为6.5元每千克

number_1 = int(input('输入购买量:'))

if number_1 > 10:
    print(price_2 * number_1)
else:
    print(price_1 * number_1)


