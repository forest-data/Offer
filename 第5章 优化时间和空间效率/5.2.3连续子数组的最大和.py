# coding=utf-8
"""
连续子数组的最大和
思路 > 采用的是当且叠加的结果，与下一次叠加的结果进行对比。
动态规划问题
"""

def max_sum(lis):

    ret = float('-inf')   # 负无穷

    if not lis:
        return ret

    curr = 0

    for i in lis:
        if curr <= 0:
            curr = i

        else:
            curr += i

        ret = max(ret, curr)

    return ret

if __name__ == "__main__":
    test = [1, 2, -2, -3, 6, 0, -2]
    print(max_sum(test))