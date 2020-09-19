# def canThreePartsEqualSum(A):
#     if len(A) < 3:
#         return False

#     p = sum(A)/3
    
#     temp = 0
#     for i in range(len(A)):
#         temp += A[i]
#         if temp == p:
#             first = i
#             break
#     else:
#         return False
    
#     temp = 0
#     for j in range(first+1,len(A)):
#         temp += A[j]
#         if temp == p:
#             second = j
#             break
#     else:
#         return False
    
#     if not A[second+1:]:
#         return False
#     else:
#         return sum(A[second+1:]) == p


def canThreePartsEqualSum(A):
    s = sum(A)
    if s % 3 != 0:
        return False
    target = s // 3
    n, i, cur = len(A), 0, 0
    while i < n:
        cur += A[i]
        if cur == target:
            break
        i += 1
    if cur != target:
        return False
    j = i + 1
    while j + 1 < n:  # 需要满足最后一个数组非空
        cur += A[j]
        if cur == target * 2:
            return True
        j += 1
    return False

print(canThreePartsEqualSum([1,-1,1,-1]))