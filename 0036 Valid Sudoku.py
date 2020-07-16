import numpy as np

def isValidSudoku(board):
    board = np.array(board)
    rows, columns = board.shape
    
    for row in range(rows):
        temp = [i for i in board[row] if i != '.']
        if len(temp) != len(set(temp)):
            return False
        
    for column in range(columns):
        temp = [i for i in board.T[column] if i != '.']
        if len(temp) != len(set(temp)):
            return False
    
    for g_row in range(0,row,3):
        for g_column in range(0,columns,3):
            temp = board[g_row:g_row+3,g_column:g_column+3].reshape(1,9)[0]
            temp = [i for i in temp if i != '.']
            if len(temp) != len(set(temp)):
                return False
    return True


print(isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))