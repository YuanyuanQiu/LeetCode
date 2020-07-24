# import numpy as np

# def rotate(matrix):
#     n = len(matrix)
    
#     if n <= 1:
#         return matrix
    
#     new_matrix = np.zeros(shape=[n,n])
#     for i in range(n):
#         for j in range(n):
#             new_matrix[j][n-1-i] = matrix[i][j]
    
#     return new_matrix

def rotate(matrix):
    n = len(matrix[0])        
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
    
    # reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix



print(rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))