#def islandPerimeter(self, grid: List[List[int]]) -> int:
#    row = len(grid)
#    col = len(grid[0])
#    directions = [(-1,0),(1,0),(0,-1),(0,1)]
#    res = 0
#    for i in range(row):
#        for j in range(col):
#            if grid[i][j] == 1:
#                if i == 0:
#                    res += 1
#                if i == row - 1:
#                    res += 1
#                if j == 0:
#                    res += 1
#                if j == col - 1:
#                    res += 1
#                for d in directions:
#                    if i + d[0] >= 0 and i + d[0] < row and j + d[1] >= 0 and j + d[1] < col and grid[i + d[0]][j + d[1]] == 0:
#                        res += 1
#    
#    return res


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