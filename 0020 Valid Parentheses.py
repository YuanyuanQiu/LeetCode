# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:04:38 2020

@author: ToxicCat
"""

def isValid(s: str) -> bool:
    '''字典key:value
    栈：遍历每个元素，若左放入字符串，若右则匹配字符串最后一个是否登对，是则去掉,
    否则False    
    '''    
    dict1={'(':')','{':'}','[':']'}
    result = True
    if s == '':
        return True
    if len(s)%2 !=0:
            return False
    ls = []
    for i in s:
        if i in dict1.keys():
            ls.append(i)
        else:
            if ls == []:
                return False
            elif dict1[ls[-1]] != i:
                return False
            else:
                del ls[-1]
    if ls != []:
        return False
    return result

print(isValid("){"))
            
    