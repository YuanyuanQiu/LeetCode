# # 暴力法
# def hasGroupsSizeX(deck):
#     count = {}
#     for i in deck:
#         count[i] = count.get(i,0) + 1

#     N = len(deck)
#     for X in range(2, N+1):
#         # X是否为N的约数
#         if N % X == 0:
#             # X是否为每一个GROUP的约数
#             if all(v % X == 0 for v in count.values()):
#                 return True
#     return False

def gcd(a,b):
    # a作为除数 必须大于b
    if a < b:
        a, b = b, a
    while b:
        a,b = b,a%b
    return a


# 最大公约数
def hasGroupsSizeX(deck):
    # math.gcd求两个数的最大公约数，返回整数
    # from math import gcd
    # collections.Counter统计字符串（数字）种类及数量，返回字典
    from collections import Counter
    # functools.reduce逐次对上次函数结果与当前序列元素应用函数
    from functools import reduce 
    
    vals = Counter(deck).values()
    return reduce(gcd, vals) >= 2

print(hasGroupsSizeX([1,2,3,4,4,3,2,1]))