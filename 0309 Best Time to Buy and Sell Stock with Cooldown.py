class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0]: 持有股票，max(dp[i-1][0], dp[i-1][2] - prices[i])
        # dp[i][1]：不持有股票，处于冷冻期，dp[i-1][0] + prices[i]
        # dp[i][2]：不持有股票，不处于冷冻期，max(dp[i-1][2], dp[i-1][1])
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0 for _ in range(3)] for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        return max(dp[n-1][1], dp[n-1][2])