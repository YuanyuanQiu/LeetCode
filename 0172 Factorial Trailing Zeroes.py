# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 03:42:29 2020

@author: ToxicCat
"""

def trailingZeroes(n):
    count=0
    while n>0:
        count+=n//5
        n=n//5
    return count

print(trailingZeroes(30))