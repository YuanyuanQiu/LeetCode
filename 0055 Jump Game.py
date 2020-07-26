# def canJump(nums):   
#     ls = []
#     for i,v in enumerate(nums):
#         ls.append(i+v)
#         if len(ls) > 1:
#             if max(ls[:-1]) < i:
#                 return False
#     return True


def canJump(nums):   
    n, rightmost = len(nums), 0
    for i in range(n):
        # 只遍历还未到达rightmost的部分
        if i <= rightmost:
            rightmost = max(rightmost, i + nums[i])
            if rightmost >= n - 1:
                return True
    return False

print(canJump([3,2,1,0,4]))
            
            