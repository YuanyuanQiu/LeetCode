def findMatrix(a):
    n = len(a)
    m = len(a[0])
    b = [[0 for _ in range(m)] for _ in range(n)]
    
    b[0][0] = a[0][0]
    for i in range(1,n):
        b[i][0] = b[i-1][0] + a[i][0]
    for j in range(1,m):
        b[0][j] = b[0][j-1] + a[0][j]
    
    for i in range(1,n):
        for j in range(1,m):
            b[i][j] = b[i-1][j] + b[i][j-1] + a[i][j] - b[i-1][j-1]
    
    return b

print(findMatrix([[1,2,3],[4,5,6]]))