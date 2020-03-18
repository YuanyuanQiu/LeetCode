# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:44:01 2020

@author: ToxicCat
"""

def countPrimes(n):
    if n<=2:
        return 0
    elif n==3:
        return 1
    else:
        ls=[1]*n # 0至n-1
        ls[0]=0
        ls[1]=0
        for i in range(2,n): #选定数i
#            for j in range(pow(i,2),n): #选定数j是否i的倍数
#                if ls[j] and j%i==0:
#                    ls[j]=0
            if ls[i]:
                a=len(ls[i*i:n:i])
                ls[i*i:n:i]=[0]*a
        count=ls.count(1)
    return(count)

print(countPrimes(10))