# coding=utf-8
# 二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
# 从左下角（或右上角）开始遍历数组


def find_num(matrix, num):
    # matrix ： 二维数组
    # num ：一个数

    if not matrix:    # matrix = [[]]
        return False

    # 采用右上角思路

    # 初始行列坐标
    row, col = 0, len(matrix[0])-1

    while row <= len(matrix)-1 and col <= len(matrix[0])-1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            col -= 1
        else:
            row += 1

    return False    # 如果没有找到




if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [2, 3, 6],
              [3, 6, 7]]
    num = 8
    print(find_num(matrix, num))