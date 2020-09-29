
# 题目：把字符串中的空格替换成'20%'
# 方法1：直接使用Python字符串的内置函数
# 方法2: 使用正则表达式

# 方式一
print("a b  c ".replace(" ", '*'))

# 方式二
import re
ret = re.compile(' ')
print(ret.sub('*', ' a b  c'))