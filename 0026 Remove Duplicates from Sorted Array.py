# def removeDuplicates(nums):
#     if len(nums) <= 1:
#         return len(nums)
    
#     l = 1
#     while l < len(nums):
#         if nums[l] == nums[l-1]:
#             nums.remove(nums[l])
#         else:
#             l += 1
        
#     return len(nums)


def removeDuplicates(nums):
    f,s = 1,0
    while f < len(nums):
        if nums[f] != nums[s]:
            nums[s+1] = nums[f]
            s += 1
        f += 1
    return len(nums[0:s+1])


print(removeDuplicates([1,1,2,3,3]))
        