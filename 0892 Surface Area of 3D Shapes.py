def surfaceArea(self, grid):
    n = len(grid)
    res = 0
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                res += 2
                if i == 0:
                    res += grid[i][j]
                if j == 0:
                    res += grid[i][j]
                if i == n - 1:
                    res += grid[i][j]
                if j == n - 1:
                    res += grid[i][j]
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < n and 0 <= newj < n and grid[newi][newj] > grid[i][j]:
                    res += grid[newi][newj] - grid[i][j]
    return res