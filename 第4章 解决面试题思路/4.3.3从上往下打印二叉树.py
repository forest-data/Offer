# coding=utf-8
"""
从上往下打印二叉树
树的广度优先，按层次遍历，使用一个辅助队列就可以
"""
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def construct_tree(self, lis=None):

        if not lis:
            return None

        self.root = Node(lis[0])
        queue = deque([self.root])
        length = len(lis)
        nums = 1
        while nums < length:
            node = queue.popleft()

            if node:
                node.left = Node(lis[nums]) if lis[nums] else None
                queue.append(node.left)
            if nums + 1 < length:
                node.right = Node(lis[nums + 1]) if lis[nums+1] else None
                queue.append(node.right)
                nums += 1

            nums += 1

    def bfs(self):
        ret = []

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return ret


def bfs(header):
    if not header:
        return None

    stack = [header]
    ret = []
    while stack:
        node = stack.pop(0)
        ret.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ret



if __name__ == "__main__":
    t = Tree()
    t.construct_tree([1,2,3,4,5,6,7,8])
    print(t.bfs())
    print(bfs(t.root))