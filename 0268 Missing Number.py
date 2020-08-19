# def missingNumber(nums):
#     n = max(nums)
#     nums_all=list(range(n+1))
#     for i in nums:
#         nums_all.remove(i)
#     if nums_all == []:
#         return n+1
#     else:
#         return nums_all[0]


# def missingNumber(nums):
#     nums.append('Missing')

#     l = 0
#     while l < len(nums) - 1:
#         if nums[l] != 'Missing' and nums[l] != l:
#             temp = nums[l]
#             nums[l], nums[temp] =  nums[temp], nums[l]
#         else:
#             l += 1

#     return nums.index('Missing')


def missingNumber(nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number

print(missingNumber([3,0,1]))