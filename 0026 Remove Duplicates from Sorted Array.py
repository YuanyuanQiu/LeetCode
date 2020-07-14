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
    if not nums:
        return 0
    
    i = 0 
    for j in range(1, len(nums)):
        # print(i,j,nums)
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


print(removeDuplicates([1,1,2,3,3]))
        