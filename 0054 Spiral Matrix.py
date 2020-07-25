import numpy as np

def spiralOrder(matrix):
    if matrix == []:
        return []
    
    matrix = np.array(matrix)

    ls = []
    flag = [1,-1]
    while matrix.shape[0] > 0 or matrix.shape[1] > 0:
        if matrix.shape[0] > 0:
            if flag[0] == 1:
                ls = np.append(ls,matrix[0])
                matrix = matrix[1:]
                flag[0] = -1
            elif flag[0] == -1:
                ls = np.append(ls,matrix[-1][::-1])
                matrix = matrix[:-1]
                flag[0] = 1

        if matrix.shape[1] > 0:
            if flag[1] == -1:
                ls = np.append(ls,matrix[:,-1])
                matrix = matrix[:,:-1]
                flag[1] = 1
            elif flag[1] == 1:
                ls = np.append(ls,matrix[:,0][::-1])
                matrix = matrix[:,1:]
                flag[1] = -1

    return list(map(int,ls))
    

print(spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))