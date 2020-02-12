# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:14:57 2020

@author: ToxicCat
"""

def titleToNumber(s):
    origin=ord('A')
    s=s[::-1]
    col_num=0
    for i in range(len(s)):
        gap=ord(s[i])-origin
        col_num+=pow(26,i)*(1+gap)
        # print('col_num:',col_num)
    return col_num

print(titleToNumber('AA'))
        