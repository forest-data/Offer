# coding=utf-8

"""
统计一个数字在排序数组中出现的次数
使用二分法分别找到数组中第一个和最后一个出现的值的坐标，然后相减
[1, 2, 2, 3, 3, 3, 4]   3有3次
"""


# 方法一  时间复杂度O(n^2)
# lis = [1, 2, 3, 3, 3, 3, 4]
# print(lis.count(3))

# 方法二: 思想> 使用二分法分别找到数组中第一个和最后一个出现的值的坐标，然后相减
# lis 是 列表   k是列表中的值


def get_k_counts(lis, k):
    first = get_first_k(lis, k)
    last = get_last_k(lis, k)

    if first < 0 and last < 0:    # 没有这个数
        return 0

    return last - first + 1

def get_first_k(lis, k):
    left, right = 0, len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] < k:    # 中间的数，比k小
            left = mid + 1
        elif lis[mid] == k:
            if lis[mid-1] < k or mid - 1 < 0: # 如果就是第一个位置  【1 *2 2 2 3】, 有一种情况就是lis[mid - 1] 报 IndexError  【*2 2 2 】
                return mid
            if lis[mid-1] == k or mid - 1 < 0:  # 如果指的是中间或后面的位置，再进行循环 【1 2 *2 2 3】
                right = mid - 1
        elif lis[mid] > k:   # 中间的数，比k大
            right = mid - 1
    return -1    # 表示未找到该数

def get_last_k(lis, k):
    left, right = 0, len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] < k:    # 中间的数，比k小
            left = mid + 1
        elif lis[mid] == k:
            if mid + 1 == len(lis):    # 有一种情况就是lis[mid + 1] 报 IndexError  【1 2 2 *2】
                return mid
            if lis[mid+1] > k :    # 如果mid表最后一个位置  【1 2 2 *2 3】 lis[mid+1] > k ,
                return mid
            if lis[mid+1] == k and mid <= len(lis):  # 如果指的是中间或前面的位置，再进行循环 【1 2 *2 2 3】
                left = mid + 1                    
        elif lis[mid] > k:   # 中间的数，比k大
            right = mid - 1
    return -1    # 表示未找到该数

if __name__ == '__main__':
    lis = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    print(get_k_counts(lis, 1))
