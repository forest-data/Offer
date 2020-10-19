# coding=utf-8
"""
翻转一个英文句子中的单词顺序，标点和普通字符一样处理
Python中字符串是不可变对象，不能用书中的方法，可以直接转化成列表然后转回去
"""


def reverse_words(words):
    tmp = words.split(" ")   # 根据空格分隔 ['I', 'am', 'a', 'engineer.']
    print(tmp)
    return ' '.join(tmp[::-1])

if __name__ == "__main__":
    test = 'I am a engineer.'
    print(reverse_words(test))

# coding=utf-8
"""
把字符串的前面的若干位移到字符串的后面
"""


def rotate_string(s, n):
    if not s:
        return ''
    n %= len(s)
    return s[n:] + s[:n]

if __name__ == '__main__':
    test = 'abcdefg'
    print(rotate_string(test, 1))
