def shortestPath(grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    # 这条路径上最多只会有 m + n - 3 个障碍物
    k = min(k, m+n-3)
    directs = [[1,0],[-1,0],[0,1],[0,-1]]
    que = [[0,0,k]]
    len_que = 1
    steps = 0
    visited = {(0,0):k}
    while que:
        for _ in range(len_que):
            x,y,k_cur = que.pop(0)
            if x==m-1 and y==n-1: return steps
            for d in directs:
                if 0<=x+d[0]<m and 0<=y+d[1]<n and k_cur-grid[x+d[0]][y+d[1]]>=0:
                    # 此前未到达
                    if (x+d[0], y+d[1]) not in visited: 
                        que.append([x+d[0], y+d[1], k_cur-grid[x+d[0]][y+d[1]]])
                        visited.update({(x+d[0], y+d[1]):k_cur-grid[x+d[0]][y+d[1]]})
                    # 此前经过 但是这次剩余k更大 
                    elif (x+d[0], y+d[1]) in visited and \
                        k_cur-grid[x+d[0]][y+d[1]]>visited[(x+d[0], y+d[1])]: 
                        que.append([x+d[0], y+d[1], k_cur-grid[x+d[0]][y+d[1]]])
                        visited[(x+d[0], y+d[1])]=k_cur-grid[x+d[0]][y+d[1]]
        len_que = len(que)
        steps+=1
    # que为空 无路可走 未到终点
    return -1