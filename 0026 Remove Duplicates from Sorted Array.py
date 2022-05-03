def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n
    l, r = 1, 1
    while r < n:
        if nums[r] != nums[r-1]: #说明nums[r]和之前元素都不同
            nums[l] = nums[r]
            l += 1
        r += 1
    return l