'''
买入：次日价格高于本日价格则买入，小于则跳过
卖出：买入后价格高于BKPRICE，存入，若后一天价格高于该日价格则更新，小于则计算利润
'''

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        tmp = prices[i] - prices[i - 1]
        if tmp > 0:
            profit += tmp
    return profit



print(maxProfit([7,1,5,3,6,4]))
    
    