def longestIncreasingPath(matrix):
    m, n = len(matrix), len(matrix[0])
    if m == 1 and n == 1:
        return 1
    record = [[0] * n for _ in range(m)] # 存储从（i，j）出发的最长递归路径
    res = 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(i, j):
        nonlocal res
        compare = [] # store path length for each direction
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                if record[x][y]: # if path length is known
                    compare.append(record[x][y])
                else: # if path length is unknown
                    compare.append(dfs(x, y))
        # max neighbor path length + 1
        record[i][j] = max(compare) + 1 if compare else 1
        # update max result
        res = max(res, record[i][j])
        return record[i][j]

    for i in range(m):
        for j in range(n):
            if not record[i][j]:
                dfs(i, j)

    return res