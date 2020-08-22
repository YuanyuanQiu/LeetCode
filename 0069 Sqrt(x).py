'''
平方根不会大于本身的一半（4：等于一半；0,1,2,3：小于一半）
二分法：左边界：0；右边界：x//2+1（照顾1）
'''

# def mySqrt(x):
#     l,r = 0, x//2 + 1
#     while l <= r:
#         m = l + (r - l)//2
#         if m * m <= x and (m+1) * (m+1) > x:
#             return m
#         elif m * m > x:
#             r = m
#         elif (m+1) * (m+1) <= x:
#             l = m + 1
#     return m

def mySqrt(x):
    left = 0
    right = x//2+1
    while left < right:
        mid = left + (right-left)//2+1 #取右中位数
        square = mid * mid
        if square>x:
            right = mid-1
        else:
            left = mid
    return left
        



print(mySqrt(4))