# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:28:21 2020

@author: ToxicCat
"""

'''
递归
'''

def countAndSay(n: int) -> str:
    if(n == 1): return '1'
    num = countAndSay(n-1)+"*" #递归，直到最小数字1
    #print(num)
    temp = num
    count = 1 #计数器
    strBulider = '' #字符串，记录最终结果
    #print(len(temp))
    for i in range(len(temp)-1): #对除了最后一位*进行遍历
        if  temp[i] == temp[i+1]: #假设该位与后一位相同
                count += 1 #计数器加1
        else: #若该位与后一位不同，count复位为1
            strBulider +=  str(count) + temp[i] #count个i
            count = 1
    return strBulider

print(countAndSay(5))
        