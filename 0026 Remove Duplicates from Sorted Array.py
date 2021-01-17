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
    p, q = 0, 1
    while q < len(nums):
        if nums[p] == nums[q]:
            q = q + 1
        else:
            nums[p+1] = nums[q]
            p = p + 1
            q = q + 1
    return len(nums[0:p+1])


print(removeDuplicates([1,1,2,3,3]))
        