import numpy as np

def solveSudoku(board):
    board = np.array(board)
    rows, columns = board.shape
    
    while '.' in board.flatten():
        for row in range(rows):
            r = set(board[row])
            if '.' in r:
                r.remove('.')
    
            for column in range(columns):
                if board[row][column] == '.':
                    
                    c = set(board.T[column])
                    if '.' in c:
                        c.remove('.')
        
                    g_row = row//3*3
                    g_col = column//3*3
                    grid = set(board[g_row:g_row+3,g_col:g_col+3].reshape(1,9)[0])
                    if '.' in grid:
                        grid.remove('.')
        
                    combine = r | c | grid
                    candidates = {'1','2','3','4','5','6','7','8','9'} - combine
                    
                    if len(candidates) == 1:
                        board[row][column] = list(candidates)[0]
                        break

    return board

    

print(solveSudoku([
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