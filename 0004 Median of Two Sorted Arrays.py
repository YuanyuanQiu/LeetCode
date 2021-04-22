def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    n1, n2 = len(nums1), len(nums2)
    length = n1 + n2
    if length % 2 != 0:
        mid1 = mid2 = length // 2
    else:
        mid1, mid2 = length // 2 - 1, length // 2
    
    sortlist = []
    while nums1 and nums2:
        if nums1[0] < nums2[0]:
            sortlist.append(nums1[0])
            nums1 = nums1[1:]
        else:
            sortlist.append(nums2[0])
            nums2 = nums2[1:]
        if len(sortlist) == mid2 + 1:
            return (sortlist[mid1] + sortlist[mid2]) / 2
    if nums1:
        sortlist = sortlist + nums1
    if nums2:
        sortlist = sortlist + nums2
    
    return (sortlist[mid1] + sortlist[mid2]) / 2