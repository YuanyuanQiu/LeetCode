# def intersect(nums1, nums2):
#     intersection = []
#     for i in nums1:
#         if i in nums2:
#             intersection.append(i)
#             nums1[nums1.index(i)]='x'
#             nums2[nums2.index(i)]='x'
#     return intersection
            
def intersect(nums1, nums2):
    hash = {}
    for num in nums1:
        if num not in hash:
            hash[num] = 1
        else: 
            hash[num] += 1

    res = []
    for num in nums2:
        if num in hash and hash[num] > 0:
            res.append(num)
            hash[num] -= 1
    return res


print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))