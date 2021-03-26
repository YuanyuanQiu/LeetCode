class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # buy[i][k]: 第i天持有完成k次
        # sell[i][k]: 第i天不持有完成k次
        n = len(prices)
        if n <= 1:
            return 0
        k = min(k, n // 2)
        
        # 初始化
        buy = [[0 for _ in range(k+1)] for _ in range(n)]
        sell = [[0 for _ in range(k+1)] for _ in range(n)]
        # 边界不合法，第0天完成1笔及以上交易
        for i in range(1,k+1):
            buy[0][i] = float('-inf')
            sell[0][i] = float('-inf')
        buy[0][0] = -prices[0]
        sell[0][0] = 0 # 第1天没有完成任何交易，可省略

        for i in range(1,n):
            # from buy[1][0]
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            sell[i][0] = 0 # 第i天没有完成任何交易，可省略
            for j in range(1,k+1):
                # from buy[1][1] and sell[1][1]
                buy[i][j] = max(buy[i-1][j], sell[i-1][j] - prices[i])
                sell[i][j] = max(sell[i-1][j], buy[i-1][j-1] + prices[i])
                
        return max(sell[n-1])