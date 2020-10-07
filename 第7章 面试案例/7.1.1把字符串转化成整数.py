# coding=utf-8
"""
把字符串转化成整数
测试用例：正负数和0，空字符，包含其他字符
备注：使用raise抛出异常作为非法提示
"""


def str_to_int(string):
    if not string:
        raise Exception('String can not be None', string)

    flag = 0   # 用来表示第一个字符是否为 + -
    ret = 0   # 结果

    for k, s in enumerate(string):
        if s.isdigit(): # Python isdigit() 方法检测字符串是否只由数字组成
            val = ord(s) - ord('0')   # >>> ord('a')  97
            ret = ret * 10 + val
        else:
            if not flag:
                if s =="+" and k==0:    # 避免中间出现 + -
                    flag = 1
                elif s=="-" and k==0:
                    flag = -1
                else:
                    raise Exception('digit is not Conform rules: ', string)
            else:
                raise Exception('digit is not Conform rules: ', string)

    if flag and len(string) == 1:   # 判断是不是只有 + -
        raise Exception('digit is not Conform rules: ', string)

    return ret if flag >= 0 else -ret

if __name__ == '__main__':
    test = '12399'
    print(str_to_int(test))