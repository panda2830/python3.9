"""
输入两个整数求它的
最大公约数和最小公倍数
"""
number_1 = int(input("输入两个数值,1:"))
number_2 = int(input("输入两个数值,chapter2:"))
max_n = max(number_1, number_2)
min_n = min(number_1, number_2)
gcd_n = 0
lcm_n = 0
for i in range(1, max_n + 1):
    if (number_1 % i == 0) and (number_2 % i == 0):
        gcd_n = i
while True:
    if (min_n % number_1 == 0) and (min_n % number_2 == 0):
        lcm_n = min_n
        break
    min_n += 1

print("整数{0}和{1}的最大公约数为{2}，最小公倍数为{3}".format(number_1, number_2, gcd_n, lcm_n))
