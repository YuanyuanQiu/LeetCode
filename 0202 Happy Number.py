# def isHappy(n):
#     if n<=0:
#         return False
#     else:
#         step=0
#         while n!=1:
#             sum_square=0
#             for i in str(n):
#                 sum_square += pow(eval(i),2)
#                 n=sum_square
#             step+=1
#             if step>100:
#                 break
#     if n==1:
#         return True
#     else:
#         return False


'''
若给定数为快乐数，则最终结果为 1，若不是则进入死循环。
因此循环终止条件为 sum = 1；
将每次 sum 值存入 issam 中，利用set去重，若出现重复，则 return False
'''
def isHappy(n):
    issam = [n]
    while n != 1:
        a = list(str(n))
        n = 0
        for i in a:
            n += pow(int(i),2)
        issam.append(n)
        if len(issam) != len(set(issam)):
            return False
    return True

print(isHappy(19))