# 要求：数组中除了两个只出现一次的数字外，其他数字都出现了两遍
# 思路: 按位异或，在得到的值中找到二进制最后一个1，然后把数组按照该位是0还是1分为两组

def get_only_one_num(lis):
    if not lis:
        return None

    # 这里存在疑点



# print(3>>2)  # 0  0011 >> 2  == 0000  0
# print(3&3)   # 3  0011 & 0011  == 0011  3

# 得到第一个1的位置
def get_bin(num):
    ret = 0
    while num & 1 == 0 and ret < 32:    # 0011 & 0001  ret = 0 表第0位置 是第一个1
        num = num >> 1
        ret += 1

    return ret

# 验证t位是不是1, 是真就返回 1   是假则返回0
def is_one(num, t):
    num = num >> t
    return num & 0x01

# 自创
def get_only_one_num_(lis):
    tmp_ret = []
    for i in lis:
        if lis.count(i) == 1:
            tmp_ret.append(i)
    return tmp_ret

if __name__ == '__main__':
    # lis = [1, 2, 3, 4, 3, 1, -1, -1]
    # print(get_only_one_num_(lis))

    print(get_bin(4))   # ret = 2
    print(is_one(4,1))

