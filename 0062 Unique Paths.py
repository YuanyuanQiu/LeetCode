class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for k in range(1,m):
            for l in range(1,n):
                dp[k][l] = dp[k-1][l] + dp[k][l-1]
                
        return dp[m-1][n-1]