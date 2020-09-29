# 要求：用两个栈实现队列，分别实现入队和出队操作
# 思路：一个栈负责入队，另一个负责出队，出栈为空则从入栈中导入到出栈中




# coding=utf-8
"""
用两个栈实现队列

栈: 先进后出
队列: 先进先出
"""

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        # while 将 栈1的内容，反向添加到栈2，且返回的是 栈2的值。
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop() if self.stack2 else u'队列为空'

if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.pop())
    print(q.pop())
    print(q.pop())

