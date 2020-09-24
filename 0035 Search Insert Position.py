# def searchInsert(nums, target):
#     if target in nums:
#         result = nums.index(target)
#     else:
#         if target>nums[-1]:
#             result = len(nums)
#         elif target<nums[0]:
#             result = 0
#         else:
#             for i in range(len(nums)):
#                 if nums[i]<target and nums[i+1]>target:
#                     result = i+1
#     return result

# 二分法
def searchInsert(nums, target):
    size = len(nums)
    if size == 0:
        return 0
    
    left = 0
    right = size # 因为有可能数组的最后一个元素的位置的下一个是我们要找的
    
    while left < right:
        mid = left + (right - left) // 2 #取中间数
        if nums[mid] < target:
            left = mid + 1 # +1避免区间只有2个数时left=mid，进入死循环
        else:
            right = mid #若中间数大于target，中间数为右边界
    
    return left

print(searchInsert([1,3,5,6],2))