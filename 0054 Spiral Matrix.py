def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    res = []
    direction = [0,1]
    # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # i = j, j = -i
    i, j = 0, 0
    for k in range(m * n):
        res.append(matrix[i][j])
        visited[i][j] = True
        newi, newj = i + direction[0], j + direction[1]
        if 0 <= newi < m and 0 <= newj < n and not visited[newi][newj]:
            i, j = newi, newj
        else:
            direction[0], direction[1] = direction[1], -direction[0]
            i, j = i + direction[0], j + direction[1]
    return res