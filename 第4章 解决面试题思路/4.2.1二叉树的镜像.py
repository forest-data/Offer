# coding=utf-8
"""
问题: 什么是二叉树镜像 ？ https://blog.csdn.net/dawn_after_dark/article/details/80850422
求二叉树的镜像
思路一：按层次遍历，每一层从右到左
思路二：递归遍历
"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None


    def construct_tree(self, lis = None):

        if not lis:
            return None

        self.root = TreeNode(lis[0]) if lis[0] else None
        queue = deque([self.root])   # 将值存入队列中
        length = len(lis)
        n = 1

        while n < length:
            node = queue.popleft()
            if node:
                node.left = TreeNode(lis[n]) if lis[n] else None
                queue.append(node.left)
                if n+1 < length:
                    node.right = TreeNode(lis[n+1]) if lis[n+1] else None
                    queue.append(node.right)
                    n += 1
                n += 1

    #  广度优先遍历
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



# 思路一：按层次遍历，每一层从右到左
def mirror_bfs(root):
    ret = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            ret.append(node.val)
            queue.append(node.right)
            queue.append(node.left)

    return ret



# 思路二：递归遍历
def mirror_pre(root):
    ret = []

    def traversal(root):
        if root:
            ret.append(root.val)
            traversal(root.right)
            traversal(root.left)

    traversal(root)

    return ret


if __name__ == '__main__':
    t = Tree()
    t.construct_tree([1, 2, 6, 4, 3, 7, 5])
    print(t.bfs())
    print(mirror_bfs(t.root))
    print(mirror_pre(t.root))



