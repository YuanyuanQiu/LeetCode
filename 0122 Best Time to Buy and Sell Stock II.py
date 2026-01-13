# Option 1: Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        
        # 从第 1 天（索引1）开始，回头看前一天
        for i in range(1, len(prices)):
            # 今天的价格 - 昨天的价格
            diff = prices[i] - prices[i-1]
            
            # 如果是正数（涨了），我们就把它加到利润里
            # 如果是负数（跌了），我们就不加（相当于 max(0, diff)）
            if diff > 0:
                total_profit += diff
                
        return total_profit

# Option 2 动态规划 (DP)
# 动态规划就是状态机
# dp[i][j]表示最大现金；每天结束时有两种状态——手里有股票和没股票
# dp[i][0] - 第i天的状态0：手里没股票 = max(昨天没股票，昨天有今天卖）
# dp[i][1] - 第i天的状态1：手里有股票 = max(昨天有股票，昨天没今天买)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 1: # 边界处理，n=0或n=1时
            return 0
            
        dp = [[0] * 2 for _ in range(n)]
        # 初始化
        dp[0][0] = 0            # 第0天不持有，没赚没赔
        dp[0][1] = -prices[0]   # 第0天持有，肯定是买入，现金减少
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            
        return dp[-1][0] # 最后肯定是不持有股票赚得多
    
# Option 3 动态规划 (DP) Space Optimization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        cash = 0            # dp[i-1][0]
        hold = -prices[0]   # dp[i-1][1]
        
        for i in range(1, len(prices)):
            # 这里的顺序不重要，因为我们用到的是上一轮的值
            # 但如果怕覆盖，可以用临时变量 new_cash, new_hold
            new_cash = max(cash, hold + prices[i])
            new_hold = max(hold, cash - prices[i])
            
            cash = new_cash
            hold = new_hold
            
        return cash