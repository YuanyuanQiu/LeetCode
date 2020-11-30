class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)

        # dp[i][j]表示第i天，持有状态为j（0：不持有，1：持有）的最大收益
        dp = [[0]*2 for _ in range(n)]

        # 初始状态
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1,n):
            # i天结束不持有：前一天结束不持有，前一天结束持有本日卖出
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            # i天结束持有：前一天结束持有，前一天结束不持有本日买入
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[n-1][0]