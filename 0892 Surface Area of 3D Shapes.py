def surfaceArea(self, grid):
    N = len(grid)

    ans = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                # 上下表面积
                ans += 2
                # 上下左右
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                    if 0 <= nr < N and 0 <= nc < N:
                        nval = grid[nr][nc]
                    else:
                        nval = 0
                    
                    # 对于 grid[r][c] 四个方向的每个相邻值 nv 还要加上 max(v - nv, 0)
                    ans += max(grid[r][c] - nval, 0)

    return ans