# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 07:45:50 2020

@author: ToxicCat
"""

def convertToTitle(n: int) -> str:
    origin = ord('A')
    quotient = n//26
    remainder = n%26
    if remainder == 0:
        remainder = 26
        quotient -= 1
    title = chr(origin+remainder-1)
    while quotient>26:     
        remainder = quotient%26
        quotient = quotient//26
        if remainder == 0:
            remainder =26
            quotient -= 1
        title = chr(origin+remainder-1)+title
    if quotient != 0:
        title = chr(origin+quotient-1)+title
    return title

print(convertToTitle(1))