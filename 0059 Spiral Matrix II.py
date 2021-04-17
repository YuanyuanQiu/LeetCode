def generateMatrix(n):
    matrix = [[1 for _ in range(n)] for _ in range(n)]
    # (0,1) -> (1,0) -> (0,-1) -> (-1,0) -> (0,1) ...
    # i = j, j=-i
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    i, j = 0, 0
    direction = [0,1]
    val = 1
    
    while val < n * n:
        while 0 <= i + direction[0] < n and 0 <= j + direction[1] < n and\
        visited[i + direction[0]][j + direction[1]] != True:
            i += direction[0]
            j += direction[1]
            val += 1
            matrix[i][j] = val
            visited[i][j] = True
        direction[0], direction[1] = direction[1], -direction[0]
    return matrix

print(generateMatrix(3))