# coding=utf-8
"""
使用先序遍历和中序遍历的结果重建二叉树
"""

from collections import deque


# 二叉树节点定义
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树
class Tree:

    def __init__(self):
        self.root = None

    # BFS:广度优先搜索 DFS:深度优先搜索
    def bfs(self):
        ret = []
        queue = deque([self.root])    # queue 队列   deque 双端队列
        while queue:
            # pop（获取最右边一个元素，并在队列中删除）
            # remove（删除指定元素）
            node = queue.popleft()    # popleft（获取最左边一个元素，并在队列中删除）
            if node:
                ret.append(node.val)    #
                queue.append(node.left)   # 把节点左子树加入队列
                queue.append(node.right)    # 把节点右子树加入队列

        return ret

    # 前序遍历
    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:    # head不为空
                return

            ret.append(head.val)
            traversal(head.left)    # 先遍历左子树
            traversal(head.right)   # 在遍历右子树

        traversal(self.root)

        return ret


    # 中序遍历
    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return

            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    # 后序遍历
    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return

            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)

        return ret


# 构建二叉树
# preorder 先序  inorder 中序
def construct_tree(preorder=None, inorder=None):

    if not preorder or not inorder:   # 都不为空
        return None

    index = inorder.index(preorder[0])   # 先把根节点找出
    left = inorder[0:index]    # 左子树的值
    right = inorder[index+1:]    # 右子树的值

    root = TreeNode(preorder[0])
    root.left = construct_tree(preorder[1:1+len(left)], left)
    root.right = construct_tree(preorder[-len(right):], right)

    return root


if __name__ == '__main__':
    t = Tree()
    root = construct_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    t.root = root
    print(t.bfs())
    print(t.pre_traversal())
    print(t.in_traversal())
    print(t.post_traversal())
