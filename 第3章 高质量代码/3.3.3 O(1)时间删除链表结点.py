# 要求：O(1)时间删除链表结点
#
# 思路：如果有后续结点，后续结点的值前移，删除后续结点，如果没有，只能顺序查找了

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def delete_node(link, node):
    if node == link:   # 只有一个节点
        del node

    if node.next is None:    # 如果没有下一个节点
        while link:
            if link.next == node:   # node 是尾结点
                link.next = None
            link = link.next
    else:
        node.val = node.next.val
        n_node = node.next
        node.next = n_node.next
        del n_node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

