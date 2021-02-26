# def intersect(nums1, nums2):
#     intersection = []
#     for i in nums1:
#         if i in nums2:
#             intersection.append(i)
#             nums2[nums2.index(i)]='x'
#     return intersection
            
def intersect(nums1, nums2):
    dic = {}
    for num in nums1:
        dic[num] = dic.get(num,0) + 1

    res = []
    for num in nums2:
        if num in dic and dic[num] > 0:
            res.append(num)
            dic[num] -= 1
    return res


print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))