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

'''
为nums2维护一个字典，key为当前元素，value为该元素的下一个比其大的值
设置一个递减栈，当遇到更大的元素时，把栈里比他小的元素都放到字典中
查找时只需要在字典中找。时间复杂度O(n+m) 空间复杂度O(m)
'''

def nextGreaterElement(nums1, nums2):
    stack, hashmap = list(), dict()
    for i in nums2:
        while len(stack) != 0 and stack[-1] < i:
            hashmap[stack.pop()] = i
        stack.append(i)
    
    ls = []
    for i in nums1:
        ls.append(hashmap.get(i,-1))
    return ls

print(nextGreaterElement([2,4], [1,2,3,4]))