# coding=utf-8
"""
数组中出现次数超过一半的数字
思路: 使用hash，key是数字，value是出现的次数
注意: 列表的len方法的时间复杂度是O(1)
"""

# 使用字典的方式解决
def get_more_half_num(lis):
    hashes = dict()
    length = len(lis)

    for n in lis:
        hashes[n] = hashes[n] + 1 if hashes.get(n) else 1
        if hashes[n] > length/2:
            return n

if __name__ == "__main__":
    lis = [1,3,3,4,1,3,3,3]
    print(get_more_half_num(lis))