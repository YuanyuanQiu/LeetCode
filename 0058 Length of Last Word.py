# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:16:25 2020

@author: ToxicCat
"""

def lengthOfLastWord(s: str) -> int:
    if s == '':
        return 0
    else: 
        ls = s.strip().split(' ') #strip考虑末尾为空的情况
        # print(ls)
    return len(ls[-1])

print(lengthOfLastWord("a "))