# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 06:37:17 2020

@author: ToxicCat
"""

'''
双指针
'''

def twoSum(numbers, target):
    n = len(numbers)
    i = 0
    j = n-1
    while i<j:
        if numbers[i]+numbers[j] == target:
            return i+1, j+1
        elif numbers[i]+numbers[j] > target:
            j-=1
        else:
            i+=1

print(twoSum([5,25,75],100))