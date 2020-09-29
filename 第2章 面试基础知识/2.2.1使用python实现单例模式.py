class SingleTon(object):
    _instance = {}
    def __new__(cls, *args, **kwargs):

        if cls not in cls._instance :
            cls._instance[cls] = super(SingleTon, cls).__new__(cls)
        return cls._instance[cls]

class Myclass(SingleTon):

    def __init__(self, a):
        self.a = a     # 作用验证是否为同一实例。


a = Myclass(1)
b = Myclass(2)

print(a.a, b.a)



class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingleTon, cls).__new__(cls)
        return cls._instance

class Myclass(SingleTon):

    def __init__(self, a):
        self.a = a     # 作用验证

a = Myclass(1)
b = Myclass(2)

print(a.a, b.a)
