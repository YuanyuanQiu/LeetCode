def searchInsert(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) # 因为有可能数组的最后一个元素的位置的下一个是我们要找的
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1 # +1避免区间只有2个数时left=mid，进入死循环
        else:
            r = mid
    return l