# coding=utf-8
"""
从尾到头打印单链表
思路1：使用栈
思路2：递归
"""

# 节点对象
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Link(object):

    # 创建单链表
    @staticmethod
    def create_link(lis):    # lis 列表
        head = Node(0)   # 头节点
        move = head

        try:
            for li in lis:
                tmp = Node(li)    # 创建节点
                move.next = tmp    # 建立链接
                move = move.next   # 移动指针所指向的对象
        except Exception as e:
            print(e)

        return head.next


# 思路1：使用栈
def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())

# 思路2：递归
def print_link_recursion(links):
    if links:
        print_link_recursion(links.next)
        print(links.val)


if __name__ == "__main__":
    head = Link.create_link([1,2,3,4,5,6])
    print_links(head)