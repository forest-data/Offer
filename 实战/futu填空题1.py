# 填空题
# 1.
def foo(x=0, y=[]):
    y.append(x)
    return y

print(foo())    # [0]

print(foo(1, [1]))   #[1, 1]

print(foo(2))    # [0, 2]      我的答案 [2] , 单独来整没错，连起来得考虑 foo()


# 2.
class parent(object):
    x = 1

class child1(parent):
    pass

class child2(parent):
    pass

print(parent.x, child1.x, child2.x)    # 1 1 1

child1.x = 2
print(parent.x, child1.x, child2.x)    # 1 2 1

parent.x = 3
print(parent.x, child1.x, child2.x)    # 3 2 3    我的答案  3  3  3， 单独来整没错， 连起来不对

# 3.
def funcs():
    return [lambda x: i * x for i in range(4)]    # 考察的是 i 在外层作用域

print([f(2) for f in funcs()])    # 正确答案[6, 6, 6, 6]   我的答案[0, 1, 4, 6]   为什么？https://blog.csdn.net/Miss_Audrey/article/details/83583763