def islandPerimeter(grid) -> int:
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res+=4
                # left
                if i-1>=0 and grid[i-1][j]==1:
                    res-=2
                # up
                if j-1>=0 and grid[i][j-1]==1:
                    res-=2
                        
    return res

print(islandPerimeter([[1,0]]))