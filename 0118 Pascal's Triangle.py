# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:42:16 2020

@author: ToxicCat
"""

'''
numRows = 0/1/2特例
numRows > 3：首尾加1，第二位开始遍历上一层相加
'''

def generate(numRows: int):
    if numRows == 0:
        return []
    elif numRows == 1:
        result = [[1]]
    elif numRows == 2:
        result = [[1],[1,1]]
    else:
        result = [[1],[1,1]]
        i=1
        while i <=numRows-2:
            result.append([])
            for j in range(len(result[-2])-1):
                result[-1].append(result[-2][j]+result[-2][j+1])
            result[-1].insert(0,1)
            result[-1].append(1)
            i+=1
    return result

print(generate(5))
    