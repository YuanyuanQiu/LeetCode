def imageSmoother(M):
    ans = [[0] * len(M[0]) for _ in M]
    
    # 1层循环，定位目标
    for row,col in [(i,j) for i in range(len(M)) for j in range(len(M[0]))]:
        count = 0
        # 2层循环，定位目标周围
        for dx,dy in [(i,j) for i in range(row-1,row+2) for j in range(col-1,col+2)]:
            if 0 <= dx < len(M) and 0 <= dy < len(M[0]): 
                ans[row][col] += M[dx][dy]
                count += 1
        ans[row][col] //= count
    return ans

print(imageSmoother([[1, 1, 1],
                     [1, 0, 1],
                     [1, 1, 1]]))