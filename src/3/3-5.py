num = int(input('输入一个值:'))


def my_fun(number_i):
    number_1 = number_i % 10  # 求个位
    number_2 = number_i % 100 // 10  # 求十位
    number_3 = number_i % 1000 // 100  # 求百位
    if (number_1 ** 3 + number_2 ** 3 + number_3 ** 3) == number_i:
        print("True")
    else:
        print("False")


my_fun(num)
