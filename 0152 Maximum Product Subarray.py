def maxProduct(self, nums: List[int]) -> int:
    pre_max = nums[0]
    pre_min = nums[0]
    res = nums[0]
    for num in nums:
        cur_max = max(pre_max * num, pre_min * num, num)
        cur_min = min(pre_max * num, pre_min * num, num)
        res = max(cur_max, res)
        pre_max = cur_max
        pre_min = cur_min
    return res