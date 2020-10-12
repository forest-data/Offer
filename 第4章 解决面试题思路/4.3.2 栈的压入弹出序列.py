# 要求：判断给定的两个序列中，后者是不是前者的弹出序列，给定栈不包含相同值
# 思路：使用一个辅助栈, 如果辅助栈栈顶元素不等于出栈元素，则从入栈中找改值，直到入栈为空
# 如果最后出栈序列为空，则是入栈的弹出序列值
'''
举例：
入栈1,2,3,4,5
出栈4,5,3,2,1
首先1入辅助栈，此时栈顶1≠4，继续入栈2
此时栈顶2≠4，继续入栈3
此时栈顶3≠4，继续入栈4
此时栈顶4＝4，出栈4，弹出序列向后一位，此时为5，,辅助栈里面是1,2,3
此时栈顶3≠5，继续入栈5
此时栈顶5=5，出栈5,弹出序列向后一位，此时为3，,辅助栈里面是1,2,3
….
依次执行，最后辅助栈为空。如果不为空说明弹出序列不是该栈的弹出顺序。
'''


def pop_order(push_stack, pop_stack):

    if not push_stack or not pop_stack:
        return False

    stack = []

    while pop_stack:    #
        pop_val = pop_stack[0]    # 弹出栈第一个值

        if stack and stack[-1] == pop_val:
            stack.pop()
            pop_stack.pop(0)
        else:
            # 入栈 元素 进入 辅助栈
            while push_stack:
                if push_stack[0] != pop_val:    # 入栈元素 不等于 出栈元素
                    stack.append(push_stack.pop(0))    # 将入栈元素 存入 辅助栈中
                else:    # 如果相等， 那么就直接将 入栈 和 出栈的元素删除。
                    push_stack.pop(0)
                    pop_stack.pop(0)
                    break

        if not push_stack:    # 如果栈不为空，那么
            while stack:
                if stack.pop() != pop_stack.pop(0):
                    return False

    if not pop_stack:    # 如果
        return True

    return False




if __name__ == '__main__':
    print(pop_order([1, 2, 3], [2, 3, 1]))
