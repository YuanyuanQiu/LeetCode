# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 08:13:55 2020

@author: ToxicCat
"""

# def majorityElement(nums):
#     n = len(nums)
#     dic = {}
#     for i in nums:
#         if i not in dic:
#             dic[i]=0
#         dic[i]+=1
#         if dic[i]>n/2:
#             return i

'''
一个随机的下标很有可能存有众数
'''

import random

def majorityElement(nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate



print(majorityElement([3,2,3]))