# def findUnsortedSubarray(nums):
#     origin = nums.copy()
#     nums.sort()
#     if origin == nums:
#         return 0
#     for i in range(len(nums)):
#         if nums[i] != origin[i]:
#             start = i
#             break
#     else:
#         return 0
    
#     for j in range(len(nums)):
#         if nums[::-1][j] != origin[::-1][j]:
#             end = j
#             break
    
#     return len(nums)-end-start


# def findUnsortedSubarray(nums):
#     if len(nums) <= 1:
#         return 0

#     nums_sorted = nums.copy()
#     nums_sorted.sort()

#     l = 0
#     r = len(nums) - 1

#     while l <= r:
#         if nums[l] == nums_sorted[l]:
#             l += 1
#         else:
#             break
#     if l == r:
#         return len(nums)


#     while r>l:
#         if nums[r] == nums_sorted[r]:
#             r -= 1
#         else:
#             break

#     return r - l + 1


# 获取所有当前数组与排序后数组具有不同数值的索引，最右边的索引 - 最左边的 + 1 就是结果
def findUnsortedSubarray(nums):
    diff = []
    for i, (a, b) in enumerate(zip(nums, sorted(nums))):
        if a != b:
            diff.append(i)
    print(diff)
    # diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
    
    # 这个列表可能为空，即已经有序，那么and 操作的第一个判断就过不了，返回len(diff) 即 0
    return len(diff) and max(diff) - min(diff) + 1


print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))