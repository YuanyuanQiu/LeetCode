class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]: number of path to position dp[i][j]
        # dp[i][j] = dp[i-1] + dp[j-1]

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]