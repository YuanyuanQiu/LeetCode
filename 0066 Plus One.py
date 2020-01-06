# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:53:14 2020

@author: ToxicCat
"""

def plusOne(digits):
    num_str = ''
    for i in digits:
        num_str += str(i)
    num_str = str(eval(num_str)+1)
    ls = []
    for i in num_str:
        ls.append(eval(i))
    return ls

print(plusOne([1,3,5]))