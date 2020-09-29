# 要求：把递增数组的前面部分数字移到队尾，求数组中的最小值，例如[3,4,5,6,1,2]
# 思路：使用二分法，但要考虑[1, 0, 0, 1]这种数据，只能顺序查找


# coding=utf-8
"""
求旋转数组中的最小值
旋转数组: 把一个有序数组最开始的若干个元素搬到数组的末尾,称之为数组的旋转
二分法
需要考虑[1, 0, 0, 1]这种数据，只能从头查找
"""

def find_min(lis):
    if not lis:
        return False

    length = len(lis)

    left, right = 0, length-1

    while lis[left] >= lis[right]:   # 为什么是 左边值 > 右边值呢？ 因为只需比较出了左边大于右边的就好弄了

        if right - left == 1:    # 如果 是最后一个元素
            return lis[right]

        mid = (left + right) // 2

        if lis[left] == lis[mid] == lis[right]:
            return lis[mid]
        elif lis[left] <= lis[mid]:
            left = mid
        elif lis[right] >= lis[mid]:
            right = mid

    return lis[0]

if __name__ == "__main__":
    print(find_min([2,2,4,5,6,2]))
    print(find_min([1,0,0,1]))