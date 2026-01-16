class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        res = 0
        
        # 把周围都变成0
        def bfs(start_i, start_j):
            # 1. 初始化队列，把起点放进去
            queue = collections.deque()
            queue.append((start_i, start_j))
            
            # 标记为 '0' 代表已访问（有些解法也会用 visited set，但直接改 grid 最省空间）
            grid[start_i][start_j] = '0'
            
            # 2. 只要队列不空，就一直处理
            while queue:
                r, c = queue.popleft() # 取出队头元素
                
                # 检查上下左右四个方向
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    
                    # 3. 如果坐标合法 且 是陆地 ('1')
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        queue.append((nr, nc)) # 加入队列等待处理
                        grid[nr][nc] = '0'     # 立即标记为已访问，防止重复加入
        
        # 主循环：遍历每一个点
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j)   # 发现新岛屿，启动 BFS 把周围陆地全部铲平
                    
        return res