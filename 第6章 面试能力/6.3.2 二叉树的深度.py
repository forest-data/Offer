# coding=utf-8
"""
求二叉树的深度
思路：分别递归的求左右子树的深度
"""

# 节点
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # 构建二叉树
    def construct_tree(self, lis=None):
        if not lis:
            return None

        self.root = Node(lis[0])  # 第一个结点一定是根结点
        queue = deque([self.root])   #

        length = len(lis)

        nums = 1

        while nums < length:
            node = queue.popleft()   # 左边取出一个数   首次将根节点取出
            if node:    # 如果有根节点
                node.left = Node(lis[nums]) if lis[nums] else None    # 将根节点 指向 该节点
                queue.append(node.left)  # 将这个节点添到队列中
                if nums + 1 < length:  # 添加右节点
                    node.right = Node(lis[nums + 1])if lis[nums+1] else None
                    queue.append(node.right)
                    nums += 1

                nums += 1
        return queue

    # 广度优先遍历
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


# 求二叉树的深度
def get_depth(treenode):
    if not treenode :
        return 0

    if not treenode.left and not treenode.right: #如果没有左子树和右子树，那么只有一个根节点
        return 1

    return 1 + max(get_depth(treenode.left), get_depth(treenode.right))

# 栈实现广度优先遍历bfs
def bfs(treenode):
    if not treenode:
        return None

    stack = [treenode]    # 存放的是树节点对象
    ret = []
    while stack:
        node = stack.pop(0)     # 弹出最上方的节点
        ret.append(node.val)
        if node.left:     # 如果该节点 有指向左节点的 ，把指向的值放入栈中。 依次循环找下去
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        return ret


if __name__ == '__main__':
    t = Tree()
    t.construct_tree([1, 2, 3])
    print(t.bfs())
    print(get_depth(t.root))