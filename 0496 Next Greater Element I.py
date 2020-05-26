# def nextGreaterElement(nums1, nums2):
#     ls = []
#     for i in nums1:
#         for j in range(nums2.index(i)+1,len(nums2)):
#             if nums2[j] > i:
#                 ls.append(nums2[j])
#                 break
#         else:
#             ls.append(-1)
#     return ls

def nextGreaterElement(nums1, nums2):
    stack, hashmap = list(), dict()
    for i in nums2:
        while len(stack) != 0 and stack[-1] < i:
            hashmap[stack.pop()] = i
        stack.append(i)
    return [hashmap.get(i,-1) for i in nums1]

print(nextGreaterElement([2,4], [1,2,3,4]))