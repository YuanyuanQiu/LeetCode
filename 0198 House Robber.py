# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 06:14:58 2020

@author: ToxicCat
"""

def rob(nums):
    cur,pre = 0,0
    for i in nums:
        cur,pre = max(pre+i,cur),cur # if pre+i>cur, cur=per+i
        print(cur,pre)
    return cur

print(rob([2,7,9,3,1]))
        