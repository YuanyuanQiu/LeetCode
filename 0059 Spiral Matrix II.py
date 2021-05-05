def generateMatrix(n):
    res = [[-1 for _ in range(n)] for _ in range(n)]
    # (0,1) -> (1,0) -> (0,-1) -> (-1,0) -> (0,1) ...
    # i = j, j = -i
    m = 1
    i = j = 0
    di, dj = 0, 1
    while m <= n**2:
        res[i][j] = m
        m += 1
        newi = i + di
        newj = j + dj
        if (0 <= newi < n and 0 <= newj < n) and res[newi][newj] == -1:
            i = newi
            j = newj
        else:
            di, dj = dj, -di
            i += di
            j += dj
    return res

print(generateMatrix(3))