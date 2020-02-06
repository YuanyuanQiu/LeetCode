# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:36:36 2020

@author: ToxicCat
"""

'''
买入：次日价格高于本日价格则买入，小于则跳过
卖出：买入后价格高于BKPRICE，存入，若后一天价格高于该日价格则更新，小于则计算利润
'''

# def maxProfit(prices):
#     BKVOL = 0
#     profit = 0
#     if len(prices)==2:
#         if prices[1]>prices[0]:
#             profit = prices[1]-prices[0]
#     elif len(prices)>2:
#         for i in range(len(prices)):
#             if i!=len(prices)-1: 
#                 if BKVOL==0: #待开仓
#                     if prices[i+1]>prices[i]:
#                         BKVOL = 1
#                         BKPRICE = prices[i]
#                         #print('BKPRICE:',BKPRICE)
#                 else: #待平仓
#                     if prices[i+1]<=prices[i]:
#                         SPPRICE = prices[i]
#                         #print('SPPRICE:',SPPRICE)
#                         profit += SPPRICE - BKPRICE
#                         BKVOL=0                        
#             else:
#                 if BKVOL==1: #待平仓
#                     SPPRICE = prices[i]
#                     #print('SPPRICE:',SPPRICE)
#                     profit += SPPRICE - BKPRICE
#                     BKVOL=0
#     return profit


def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        tmp = prices[i] - prices[i - 1]
        if tmp > 0: profit += tmp
    return profit

print(maxProfit([2,1,2,0,1]))
    
    