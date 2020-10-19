# coding=utf-8
"""
求字符串中第一个只出现一次的字符   如 "abaccbdse" > 6
使用两个hash，一个记录每个字符穿线的次数，另一个记录每个字符第一次出现的位置
"""

def first_char_pos(string):

    if not string:
        return -1

    count = {}   # 记录每个字符出现的次数

    loc = {}   # 记录每一次出现的位置

    for k, s in enumerate(string):
        count[s] = count[s] + 1 if count.get(s) else 1
        loc[s] = loc[s] if loc.get(s) else k

    ret = float('inf')
    print(count)
    print(loc)
    print(loc.keys())
    for k in loc.keys():
        if count.get(k) == 1 and loc[k]<ret:
            ret = loc[k]

    return ret

if __name__ == "__main__":
    test = 'abaccbdse'
    print(first_char_pos(test))