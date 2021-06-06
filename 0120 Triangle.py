def minimumTotal(self, triangle: List[List[int]]) -> int:
    n = len(triangle)
    if n == 1:
        return triangle[0][0]
    # dp[i][j]: minimum path till triangle[i][j]
    dp = triangle.copy()
    for i in range(1,n):
        length = len(dp[i])
        for j in range(length):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == length - 1:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += min(dp[i-1][j],dp[i-1][j-1])    
    return min(dp[-1])