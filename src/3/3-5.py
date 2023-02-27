"""
编写一个函数，用平判断一个三位的整数是否是水仙花数，如153 == 1**3 + 5**3 + 3**3

"""
num = int(input('输入一个值:'))


def my_fun(number_i):
    if 100 >= number_i <= 999:  # 判断是否是3位数
        print("False")
        exit(1)
    number_1 = number_i % 10  # 求个位
    number_2 = number_i % 100 // 10  # 求十位
    number_3 = number_i % 1000 // 100  # 求百位
    if (number_1 ** 3 + number_2 ** 3 + number_3 ** 3) == number_i:
        print("True")
    else:
        print("False")


my_fun(num)
