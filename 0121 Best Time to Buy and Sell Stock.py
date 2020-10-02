def maxProfit(prices):
    # 无穷小
    minprice = float('inf')
    # 无穷大
    maxprofit = 0
    
    for price in prices:
        # 遍历过程中取得目前为止最小值
        minprice = min(minprice, price)
        # 遍历过程中取得目前为止profit最大值
        maxprofit = max(maxprofit, price - minprice)
    
    return maxprofit

print(maxProfit([7,1,5,3,6,4]))