# depth-first search
def exist(self, board: List[List[str]], word: str) -> bool:
    m = len(board)
    n = len(board[0])
    if m * n < len(word):
        return False
    
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    def dfs(i,j,history,remain,visited):
        if history == word:
            return True
        if not remain:
            return
        for di, dj in directions:
            newi, newj = i + di, j + dj
            if 0 <= newi < m and 0 <= newj < n and board[newi][newj] == remain[0] and (newi,newj) not in visited:
                if dfs(newi,newj,history + remain[0],remain[1:],visited + [(newi, newj)]):
                    return True

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if dfs(i,j,word[0],word[1:],[(i,j)]):
                    return True
    return False