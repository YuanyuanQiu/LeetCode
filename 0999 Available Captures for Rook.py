def numRookCaptures(self, board: List[List[str]]) -> int:
    cnt = 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 右下左上
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == "R":
                st, ed = i, j
    
    for i in range(4):
        step = 0 # 步数
        
        while True: # until break
            tx = st + step * dx[i]
            ty = ed + step * dy[i]
            # reaches the edge or friendly bishops
            if tx < 0 or tx >= 8 or ty < 0 or ty >= 8 or board[tx][ty] == "B":
                break
            # capture pawns
            if board[tx][ty] == "p":
                cnt += 1
                break
            
            step += 1
    return cnt