def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    visited = set()
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    
    def dfs(i,j):
        visited.add((i, j))
        for di, dj in directions:
            newi, newj = i + di, j + dj
            if 0 <= newi < m and 0 <= newj < n and board[newi][newj] == 'O' and (newi, newj) not in visited:
                dfs(newi, newj)

    for i in range(m):
        for j in range(n):
            if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                dfs(i,j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O' and (i,j) not in visited:
                board[i][j] = 'X'