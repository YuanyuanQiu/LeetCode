# def removeElement(nums, val):
#     n = len(nums)
#     if n == 0:
#         return 0
#     if n == 1:
#         if nums[0] == val:
#             return 0
#         else:
#             return 1
#     i = 0
#     j = 0
#     while j <= len(nums)-1:
#         # print(i, j, nums)
#         if nums[j] != val:
#             j += 1
#             i += 1
#         else:
#             nums.remove(nums[j])
#             j = i

#     return i

# print(removeElement([3,2,2,3], 3))


def removeElement(nums, val):
    for i in nums[:]:
        if i == val:
            nums.remove(val)
    return len(nums)