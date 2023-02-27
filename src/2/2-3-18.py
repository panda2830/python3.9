"""
求1-1000之间能被7和3整除的所有整数

"""
for i in range(1, 1000+1):
    # if i % 7 == 0 and i % 3 == 0:
    #     print(i)
    if i % 7 == 0 or i % 3 == 0:
        print(i)
        