# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:24:04 2020

@author: ToxicCat
"""

def isPalindrome(x: int) -> bool:
        if x<0: #负数为False
            return False
        else:
            m,n = x,0 #m 表示原数字，n表示反转后数字
            while m:
                n = n*10 + m%10 #m取最后一位数字，逐步前推
                m = m//10 #m去除最后一位数字（//：返回整数部分）
                
            if x == n:
                return True
            else:
                return False

print(isPalindrome(121))