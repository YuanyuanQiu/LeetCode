# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 03:15:02 2020

@author: ToxicCat
"""

# def rotate(nums, k):
#     n=len(nums)
#     if k>0:
#         for i in range(k):
#             nums.insert(0,nums[-1])
#             del nums[-1]
#     return nums
    
def rotate(nums, k):
    nums=nums[::-1]
    m=k%len(nums)
    nums=nums[:m][::-1]+nums[m:][::-1]
    return nums

print(rotate([1,3,5,7], 3))