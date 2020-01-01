# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:21:58 2020

@author: ToxicCat
"""



def reverse(x: int) -> int:
        str_x = str(x) #转化为字符串
        if str_x[0] != "-": #首位不为负号
            str_x = str_x[::-1] #反转字符串
            reverse_x = int(str_x) #转化为整数
        else: #首位为负号
            str_x = str_x[1:][::-1] #负号之后之反转字符串
            reverse_x = -int(str_x) #转化为整数
        return reverse_x if -2147483648 < reverse_x < 2147483647 else 0 #判断是否溢出

print(reverse(-1234567))