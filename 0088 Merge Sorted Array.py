# 方法一 : 合并后排序
def merge(self, nums1, m, nums2, n):
    nums1[:] = sorted(nums1[:m] + nums2)


# 方法二 : 双指针 / 从前往后
def merge(self, nums1, m, nums2, n):
    # Make a copy of nums1.
    nums1_copy = nums1[:m] 
    nums1[:] = []

    # Two get pointers for nums1_copy and nums2.
    p1 = 0 
    p2 = 0
    
    # Compare elements from nums1_copy and nums2
    # and add the smallest one into nums1.
    while p1 < m and p2 < n: 
        if nums1_copy[p1] < nums2[p2]: 
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    # if there are still elements to add
    if p1 < m: 
        nums1[p1 + p2:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]
        
# 方法三 : 双指针 / 从后往前
def merge(self, nums1, m, nums2, n):
    # two get pointers for nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    # set pointer for nums1
    p = m + n - 1
    
    # while there are still elements to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] =  nums1[p1]
            p1 -= 1
        p -= 1
    
    # add missing elements from nums2
    nums1[:p2 + 1] = nums2[:p2 + 1]