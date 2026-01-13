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