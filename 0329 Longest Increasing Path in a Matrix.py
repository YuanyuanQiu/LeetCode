def longestIncreasingPath(matrix):
    m,n = len(matrix), len(matrix[0])
    if m == 1 and n == 1:
        return 1
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    res = 0
    def dfs(history, i, j, matrix):
        nonlocal res
        print(matrix[i][j])
        if matrix[i][j] == 'seen':
            res = max(res, len(history))
        elif (not history) or (history and matrix[i][j] > history[-1]):
            val = matrix[i][j]
            matrix[i][j] = 'seen'
            print(matrix)
            for d in directions:
                newi, newj = i + d[0], j + d[1]
                if 0 <= newi < m and 0 <= newj < n:
                    print('round',newi, newj)
                    dfs(history + [val], newi, newj, matrix.copy())
    dfs([], 0, 0, matrix.copy())
    return res

print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))