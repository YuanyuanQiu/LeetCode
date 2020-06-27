# def findLengthOfLCIS(nums):
#     if len(nums) == 0:
#         return 0
#     if len(nums) == 1:
#         return 1
    
#     ls = []
#     l = 1
#     for i in range(len(nums)-1):
#         if nums[i+1] > nums[i]:
#             l += 1
#         else:
#             ls.append(l)
#             l = 1

#     ls.append(l)
#     return max(ls)

# dp[i]：表示第i个元素的递增元素个数
def findLengthOfLCIS(nums):
    n = len(nums)
    
    if not nums or n<0:
        return 0
    
    dp = [1]*n
    for i in range(1,n):
        if nums[i] > nums[i-1]:
           dp[i]=dp[i-1] + 1
    return max(dp)


print(findLengthOfLCIS([2,2,2,2,2]))