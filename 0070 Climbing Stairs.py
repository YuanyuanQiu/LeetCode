# def climbStairs(n):
#     if n < 2:
#         return 1
    
#     ans = 1
#     two = n // 2
    
#     def factorial(x):
#         if x == 0 or x == 1:
#             return 1
#         else:
#             return x*factorial(x-1)
    
#     for i in range(1,two+1):

#         if n-i*2 != 0:
#             ans += factorial(n-i*2+i)/(factorial(n-i*2+i-i)*factorial(i))
#         else:
#             ans += 1
               
#     return int(ans)

'''
1. 全1
2. 任2个相邻1合并为2
3. 最大可以有几个2(m)，遍历i in (0,m+1)个2，i个2可以有Ci/(n-2*i+i)个位置
e.g. 4
1）全1
2) 1个2：2+1+1; 1+2+1; 1+1+2; C1/3
3) 2个2: 2+2; C2/2
e.g. 5
1) 全1
2) 1个2: 2+1+1+1; 1+2+1+1; 1+1+2+1; 1+1+1+2; C1/4
3) 2个2: 2+2+1; 2+1+2; 1+2+2; C2/3
e.g. 6
1) 全1
2） 1个2: 2+1+1+1+1; C1/5
3） 2个2: 2+2+1+1; C2/4
4） 3个2: 2+2+2; C3/3
'''


def climbStairs(n: int) -> int:
    import math
    ways = 1
    m = n//2
    if m == 0:
        return ways
    else:
        for i in range(1,m+1):
            ways += math.factorial(n-2*i+i)/(math.factorial(i)*\
                                             math.factorial(n-2*i))
    return int(ways)

print(climbStairs(3))
    