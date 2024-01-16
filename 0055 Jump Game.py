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


def canJump(nums):
    n = len(nums)
    if n <= 1:
        return True
    # max index this or previous jump can reach
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        if i > dp[i-1]:
            return False
        dp[i] = max(i + nums[i], dp[i-1])
    return True

print(canJump([3,2,1,0,4]))
            
            