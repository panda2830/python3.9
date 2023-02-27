"""
输入两个整数求它

"""
number_1 = int(input("输入两个数值:1"))
number_2 = int(input("输入两个数值:2"))
gcd_n = 0
max_n = max(number_1, number_2)

for i in range(1,max_n+1):
    if number_1 % i == 0 and number_2 % i == 0:
        gcd_n = i
print(gcd_n)



