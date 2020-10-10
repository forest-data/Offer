# 2. 代码重构

# def fib(n):
#     a, b = 0, 1
#     result_list = list()
#     for _ in range(n):
#         a, b = b, a+b
#         result_list.append(a)
#
#     return result_list

def fib(index):
    n, a, b =0, 0, 1
    while n<index:
        yield b
        a, b = b, a+b
        n += 1

if __name__ == "__main__":
    # print(fib(10))
    print([x for x in fib(10)])
    
# 3. 装饰器

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

class Myclass:
    def __init__(self, v):
        self.v = v

a = Myclass(1)
b = Myclass(2)

print(a.v, b.v)
