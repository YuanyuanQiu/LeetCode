def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    def dfs(i, j):
        nonlocal count
        count += 1
        grid[i][j] = 0
        for di, dj in directions:
            newi, newj = i + di, j + dj
            if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == 1:
                dfs(newi, newj)

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                count = 0
                dfs(i,j)
                res = max(res, count)
    return res