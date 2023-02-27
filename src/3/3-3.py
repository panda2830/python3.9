"""
编写一个对列表从小到大排序的函数
"""

# 插入排序
# def insertionSort(arr):
#     for i in range(len(arr)):
#         preIndex = i-1
#         current = arr[i]
#         while preIndex >= 0 and arr[preIndex] > current:
#             arr[preIndex+1] = arr[preIndex]
#             preIndex-=1
#         arr[preIndex+1] = current
#     return arr


list_1 = [7, 4, 9, 2, 1, 0, 4]


# 冒泡排序
def my_sort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


# print(insertionSort(list_1))
print(my_sort(list_1))
