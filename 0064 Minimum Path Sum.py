class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid.copy()
        m = len(grid)
        n = len(grid[0])
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + dp[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + dp[0][j]
        
        for k in range(1,m):
            for l in range(1,n):
                dp[k][l] = min(dp[k-1][l],dp[k][l-1]) + dp[k][l]
        return dp[m-1][n-1]