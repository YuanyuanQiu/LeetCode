# depth-first search
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):            
            grid[i][j] = '0'
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == '1':
                    dfs(newi, newj)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        
        return count

# breadth-first search
'''
借用一个队列 queue，判断队列首部节点 (i, j) 是否未越界且为 1：
若是则置零（删除岛屿节点），并将此节点上下左右节点 (i+1,j),(i-1,j),(i,j+1),(i,j-1) 加入队列；
若不是则跳过此节点；
循环 pop 队列首节点，直到整个队列为空，此时已经遍历完此岛屿。
'''
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])
        
        def bfs(grid, i, j):
            queue = [[i, j]]
            while queue:
                [i, j] = queue.pop(0) # 首部节点(i,j)
                if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                    grid[i][j] = '0'
                    for di, dj in directions:
                        queue += [[i + di, j + dj]]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                bfs(grid, i, j)
                count += 1
        return count


