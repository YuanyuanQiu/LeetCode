def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = len(matrix)
    col = len(matrix[0])

    # 第一行/列作为标志位
    row0_flag = False
    col0_flag = False
    # 判断标志位本身是否有零
    # 找第一行是否有0
    for j in range(col):
        if matrix[0][j] == 0:
            row0_flag = True
            break
    # 第一列是否有0
    for i in range(row):
        if matrix[i][0] == 0:
            col0_flag = True
            break

    # 把第一行或者第一列作为标志位，更新标志位
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    #print(matrix)
    # 根据标志位置0
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # 如标志位本身有0，置0
    if row0_flag:
        for j in range(col):
            matrix[0][j] = 0
    if col0_flag:
        for i in range(row):
            matrix[i][0] = 0