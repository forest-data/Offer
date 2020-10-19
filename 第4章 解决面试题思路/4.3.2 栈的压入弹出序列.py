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


def is_order(o_stack, i_stack):
    # o_stack  出栈   i_stack 入栈

    # 如果出栈入栈不为空
    if not o_stack or not i_stack:
        return False

    stack = []

    while i_stack:

        i_val = i_stack[0]

        #
        while o_stack:
            if o_stack[0] == i_val:
                o_stack.pop(0)
                i_stack.pop(0)
                break
            else:
                stack.append(o_stack.pop(0))

        #
        if not o_stack: #如果出栈为空
            while stack:
                if stack.pop(0) != i_stack.pop(0):
                    return False


    if not i_stack:   # 如果进栈为空
        return True

    return False




if __name__ == '__main__':
    print(is_order([1, 2, 3], [2, 3, 5]))
