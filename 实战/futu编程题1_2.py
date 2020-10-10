import copy
# 编程题
# 1.假设楼梯有n个台阶，每次可以选择上一个阶梯还是两个阶梯，请问走完阶梯总共有几种走法， 参数为 楼梯阶数， 返回走法数。
# 思想: 可以使用逆向思维思考这个问题，即求出上(n-1)个台阶和(n-2)个台阶的方法总和为上n个台阶的方法数。

def footstep(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return footstep(n-1) + footstep(n-2)

if __name__ == "__main__":
    print(footstep(10))

# 2.一个整型数组，找出所有满足如下的数，所有它左边的数都比它小，所有它右边的数都比它大，
# 例如: 数组【1，2，4，3，9，5，6，12，15】， 数组中 1， 2， 12，15满足条件，时间复杂度为o(n).

# 求符合该要求的一个数
'''
思路
使用变量求解：
（1）目前找到符合题意的候选值，nCandid
（2）目前已遍历数组的最大值，nMax：为了选下一次的候选值
（3）目前的候选值是否有效，bIsExist：检测是否需要重新选择候选值
思路：如果候选值有效，可以继续遍历下面的数据
如果候选值小于目前的值，则该候选失效。之后遍历元素时，就要重新选择候选值
选择候选值时，对于某一个元素，如果该元素比之前遍历过元素的最大值还要大nMax，则该元素就为候选。
复杂度：遍历一遍数组即可，时间：O（n），空间O（1）
'''

def findnum(lis):

    n = len(lis)
    nPos = 0
    nCandid = lis[0]    # 目前找到符合题意的候选值
    nMax = lis[0]    # 目前已遍历数组的最大值,为了选下一次的候选值
    bIsExist = True    # 目前的候选值是否有效, 检测是否需要重新选择候选值

    for i in range(1, n):

        if bIsExist:    # 候选有效
            if nCandid > lis[i]:
                bIsExist = False    # 如果后一个值大，那么该数就不符合
            else:
                nMax = lis[i]     # 否则就将目前遍历的最大值改掉
        else:    # 候选无效
            # 重新找候选
            if lis[i] >= nMax:
                bIsExist = True
                nCandid = lis[i]
                nMax = lis[i]
                nPos = i

    return lis[nPos] if bIsExist else -1

# 求符合要求的所有数
"""
思路：
使用一个数组nArrMin[i]来保存[i,nLen-1]区间内的最小值。
使用一个变量nMax保存区间[0,i-1]的最大值。
对于第i个数，如果它满足nArr[i]大于左边的最大数nMax 且 小于右边的最小数nArrMin[i]，则该数即为所求。
复杂度：时间：O（n），空间O（n）
"""
def find_all_num(lis):
    nPos = 0    # 符合条件的索引
    nMax = 0    # 目前已遍历数组的最大值
    nArrMin = copy.deepcopy(lis)    # 使用列表来保存[i,nLen-1]区间内的最小值。
    n = len(lis)

    # 遍历一遍数组，记录区间[i,len]的最小值，并保存到数组nArrMin[i]中
    for i in range(len(lis)-2, 0, -1):
        if lis[i] > nArrMin[i+1]:
            nArrMin[i] = lis[i+1]
        else:
            nArrMin[i] = lis[i]

    print(nArrMin)
    print(lis)
    #遍历一遍数组，求解满足题意的数

    for i in range(n):
        if lis[i] > nMax:
            if lis[i] <= nArrMin[i]:
                # lis[i] 比左边数的最大值还要大且比右边数的最小值还要小，则输出
                print(lis[i])
            nMax = lis[i]



if __name__ == "__main__":
    lis = [1, 2, 4, 3, 9, 5, 6, 12, 15]
    find_all_num(lis)