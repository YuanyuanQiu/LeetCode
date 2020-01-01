# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:37:55 2020

@author: ToxicCat
"""

def romanToInt(s: str) -> int:
        Roman_single={}
        Roman_single["I"]=1
        Roman_single["V"]=5
        Roman_single["X"]=10
        Roman_single["L"]=50
        Roman_single["C"]=100
        Roman_single["D"]=500
        Roman_single["M"]=1000

        Roman_combined={}
        Roman_combined["IV"]=4
        Roman_combined["IX"]=9
        Roman_combined["XL"]=40
        Roman_combined["XC"]=90
        Roman_combined["CD"]=400
        Roman_combined["CM"]=900

        num=0

        for i in Roman_combined.keys(): #先剔除掉两位的并求和
            if i in s:
                s=s.replace(i,'')
                num+=Roman_combined[i]
        for j in s: #剩余字符求和
                num+=Roman_single[j]
        return num

print(romanToInt("MCMXCIV"))