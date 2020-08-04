def maxProfit(prices):
    minprice = float('inf')
    maxprofit = 0
    
    for price in prices:
        minprice = min(minprice, price)
        maxprofit = max(maxprofit, price - minprice)
    return maxprofit

print(maxProfit([7,1,5,3,6,4]))