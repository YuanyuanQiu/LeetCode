# Option 1 DP框架
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        # 初始化
        dp = [[0] * 4 for _ in range(n)]
        
        # Day 0 初始化
        dp[0][0] = -prices[0] # Buy1: 花钱买第一股
        dp[0][1] = 0          # Sell1: 还没卖，利润0
        dp[0][2] = -prices[0] # Buy2: 假设同一天买卖又买，成本还是 -price
        dp[0][3] = 0          # Sell2: 还没卖
        
        for i in range(1, n):
            # 1. Buy1: 来自 初始状态(0)
            dp[i][0] = max(dp[i-1][0], -prices[i]) 
            
            # 2. Sell1: 来自 Buy1
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            
            # 3. Buy2: 来自 Sell1 (用第一次赚的钱买)
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i])
            
            # 4. Sell2: 来自 Buy2
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] + prices[i])
            
        # 返回 Sell2 即可，因为如果不买第二次，Sell2 的逻辑里包含了 Sell1 的结果
        # (即 Buy2 没操作，Sell2 也没操作，最后数值等同于 Sell1)
        return dp[-1][3]
    
# Option 2 DP优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # 初始化状态
        # 第一次买入，还没开始操作，成本就是当天的价格
        buy1 = -prices[0] 
        # 第一次卖出，还没卖，利润为0
        sell1 = 0
        # 第二次买入，可以理解为第一天买入又卖出又买入，成本还是当天的价格
        buy2 = -prices[0]
        # 第二次卖出，利润为0
        sell2 = 0
        
        for price in prices[1:]:
            # 状态转移，注意顺序：虽然数学上是同时更新，
            # 但代码里写在同一行或者按顺序写因为依赖关系其实不影响最终结果（贪心属性）
            # 为了逻辑清晰，我们假设这四个操作在同一天可以连续发生
            
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            
            buy2 = max(buy2, sell1 - price) # 关键：用 sell1 的钱去买
            sell2 = max(sell2, buy2 + price)
            
        return sell2
'''
为什么最后返回 sell2？
即使实际最优解只交易了一次（比如一直涨），我们的逻辑也涵盖了。 比如 [1, 5]：

Day 1: buy1=-1, sell1=0, buy2=-1, sell2=0
Day 2:
buy1 保持 -1
sell1 变成 -1 + 5 = 4
buy2 变成 4 - 5 = -1 (相当于当天买了又卖)
sell2 变成 -1 + 5 = 4
'''