# def findMaxConsecutiveOnes(nums):
#     count = max_count = 0

#     for i in nums:
#         if i == 1:
#             count += 1
#         else:
#             max_count = max(max_count, count)
#             count = 0
#     return max(max_count, count)


# 字典
# def findMaxConsecutiveOnes(nums):
#     ans = 0
#     dic = {}
#     for i in range(len(nums)):
#         if nums[i] == 1:
#             dic[1] = dic.get(1,0) + 1
#         else:
#             ans = max(ans, dic.get(1,0))
#             dic[1] = 0
            
#     ans = max(ans,dic.get(1,0))
#     return ans


# split
def findMaxConsecutiveOnes(nums):
    strs = map(str, nums)
    ls = ''.join(strs).split('0')
    length = map(len, ls)
    return max(length)
            
    
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))