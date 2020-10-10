# 要求：0到n-1排成一圈，从0开始每次数m个数删除，求最后剩余的数
# 思路：当 n > 1 时： f(n,m) = [f(n-1, m)+m]%n, 当 n = 1 时： f(n,m)=0，
# *关键是推导出关系表达式

def last_num(n, m):   # n表示有几个数， 每次数到第m个位置，然后删除
    ret = 0
    if n == 1:   # 如果就一个数，那就返回0
        return 0
    for i in range(2, n+1):
        ret = (m + ret) % i   #
    return ret

if __name__ == '__main__':
    print(last_num(3, 2))