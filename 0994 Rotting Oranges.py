def orangesRotting(grid):
    row, col, time = len(grid), len(grid[0]), 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # 腐烂集合
    rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2} # 腐烂集合
    # 新鲜集合
    fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}  # 新鲜集合

    while fresh:
        print('rotten', rotten, 'fresh', fresh)
        if not rotten: return -1
        # 即将腐烂的如果在新鲜的集合中，就将它腐烂。只计算扩散后的腐烂集合
        rotten = {(i + di, j + dj) for i, j in rotten\
                  for di, dj in directions if (i + di, j + dj) in fresh} 
        fresh -= rotten # 剔除腐烂的
        time += 1

    return time


# def orangesRotting(self, grid: List[List[int]]) -> int:
#     row, col, time = len(grid), len(grid[0]), 0
#     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     queue = []
#     # add the rotten orange to the queue
#     for i in range(row):
#         for j in range(col):
#             if grid[i][j] == 2:
#                 queue.append((i, j, time))
#     # bfs
#     while queue:
#         i, j, time = queue.pop(0)
#         for di, dj in directions:
#             if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
#                 grid[i + di][j + dj] = 2
#                 queue.append((i + di, j + dj, time + 1))
#     # if there are still fresh oranges, return -1
#     for row in grid:
#         if 1 in row: return -1

#     return time

print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))