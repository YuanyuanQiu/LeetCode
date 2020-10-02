# 动态规划
def maxProfit(prices):
    n = len(prices)
    # 边界条件
    if n <= 1:
        return 0 
    
    # 初始条件dp表示profit list
    dp = [0] * n
    minprice = prices[0] 

    for i in range(1, n):
        minprice = min(minprice, prices[i])
        # 状态转移方程
        dp[i] = max(dp[i - 1], prices[i] - minprice)

    return dp[-1]

# 动态规划优化版（一次遍历）
def maxProfit(prices):
    # 初始条件dp表示profit
    minprice = float('inf') # 无穷大
    maxprofit = 0
    
    for price in prices:
        # 遍历过程中取得目前为止最小值
        minprice = min(minprice, price)
        # 状态转移方程
        maxprofit = max(maxprofit, price - minprice)
    
    return maxprofit

print(maxProfit([7,1,5,3,6,4]))