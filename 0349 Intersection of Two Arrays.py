def intersection(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    return list(s1 & s2)

print(intersection([4,9,5], [9,4,9,8,4]))