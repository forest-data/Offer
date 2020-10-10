# coding=utf-8
"""
按从外到里的顺序顺时针打印矩阵
每一圈的开始位置总是坐上角元素[0, 0], [1, 1]...
# mat = [[1, 2],
         [5, 6]]
"""

#
def print_circle(matrix, start, rows, cols, ret):
    row = rows - start - 1    # 最后一行   3
    col = cols - start - 1    # 最后一列   3

    # left->right  从左到右
    for c in range(start, col+1):      # 假设矩阵是4*4     从 1 打印到 4
        ret.append(matrix[start][c])

    # top -> bottom  从上到下
    if start < row:
        for r in range(start+1, row+1):    # 从 8 打印到 16
            ret.append(matrix[r][col])

    # right->left
    if start<row and start<col:
        for c in range(start,col)[::-1]:    # 从 16 打印到 13
            ret.append(matrix[row][c])

    # bottom -> top
    if start < row and start < col:
        for r in range(start+1, row)[::-1]:    # 从 9  打印到 5  接着进入下一轮循环
            ret.append(matrix[r][start])


#
def print_matrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    start = 0
    ret = []
    while start * 2 < rows and start * 2 < cols:
        print_circle(matrix, start, rows, cols, ret)
        start += 1
    print(ret)


if __name__ == '__main__':
    """
    mat = [[1, 2, 3],
           [5, 6, 7],
           [9, 10, 11]]
           
    mat = [[]]
    mat = [[1]]
    mat = [[1, 2, 3, 4]]
    mat = [[1], [2], [3], [4]]
    
    打印出来就是   1,2,3,7,11,10,9,5,6
    """
    # mat = [[1, 2],
    #        [5, 6]]

    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11,12],
           [13, 14, 15, 16]]
    print_matrix(mat)