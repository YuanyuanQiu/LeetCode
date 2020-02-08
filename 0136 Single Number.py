# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:20:23 2020

@author: ToxicCat
"""

'''
如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位
a⊕0=a
如果我们对相同的二进制位做 XOR 运算，返回的结果是 0
a⊕a=0
XOR 满足交换律和结合律
a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
所以我们只需要将所有的数进行 XOR 操作，得到那个唯一的数字。
'''

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    for i in nums:
        a ^= i #按位异或运算符：当两对应的二进位相异时，结果为1
    return a