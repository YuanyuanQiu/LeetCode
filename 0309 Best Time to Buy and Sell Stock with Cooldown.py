class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益

        f = [[0] * 3 for _ in range(n)]
        f[0][0] = -prices[0]
        # f[0][1] = 0
        # f[0][2] = 0

        for i in range(1, n):
            # 持有：i-1天结束已持有，或i-1天结束（即第i天）不处于冷冻期并买入
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            # 不持有且处于冷冻期：i-1天结束持有且i天卖出
            f[i][1] = f[i - 1][0] + prices[i]
            # 不持有且不处于冷冻期：i-1天结束（即第i天）不持有且处于冷冻期，或i-1天结束（即第i天）不持有且不处于冷冻期
            f[i][2] = max(f[i - 1][1], f[i - 1][2])
        
        return max(f[n - 1][1], f[n - 1][2])