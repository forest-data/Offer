# 1. 输入一棵二叉树，求该树的深度
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree_depth(self, treenode):
        if not treenode:
            return 0

        if not treenode.left and not treenode.right:
            return 1

        return 1 + max(self.tree_depth(treenode.left), self.tree_depth(treenode.right))

class Tree:

    def __init__(self):
        self.root = None

    def construct_tree(self, lis=None):
        if not lis:
            return None

        self.root = TreeNode(lis[0])
        queue = deque([self.root])

        length = len(lis)

        nums = 1

        while nums < length:
            node = queue.popleft()   # 左边去除一个数
            if node:

                node.left = TreeNode(lis[nums]) if lis[nums] else None
                queue.append(node.left)
                if nums + 1  < length:
                    node.right = TreeNode(lis[nums + 1]) if lis[nums + 1] else None
                    queue.append(node.right)
                    nums += 1

                nums += 1

        return queue






if __name__ == "__main__":

    s = Solution()
    lis = [1,2,3,4,5,6,7,8,9]
    t = Tree()
    print(t.construct_tree(lis))
    print(t.root)
    print(s.tree_depth(t.root))


