def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    
    row_l, row_r = 0, m-1
    while row_l < row_r:
        mid = row_l + (row_r - row_l + 1) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] > target:
            row_r = mid - 1
        else:
            row_l = mid
    
    col_l, col_r = 0, n-1
    while col_l <= col_r:
        mid = col_l + (col_r - col_l) // 2
        if matrix[row_l][mid] == target:
            return True
        elif matrix[row_l][mid] > target:
            col_r = mid - 1
        else:
            col_l = mid + 1
    return False