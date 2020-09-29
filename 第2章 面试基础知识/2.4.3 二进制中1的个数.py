# 要求：求一个整数的二进制表示中，1的个数
# 思路：二进制表示中，最后的那个1被减去后，低位都变为0，高位不变，按位与就可以去掉这个1
#  10 二进制  1010    9 二进制  1001    10 & 9  == 8


def num_of_1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n-1
    return ret

if __name__ == '__main__':
    print(bin(100))
    print(bin(100).count('1') == num_of_1(100))