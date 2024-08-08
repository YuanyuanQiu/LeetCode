def summaryRanges(self, nums: List[int]) -> List[str]:
    if not nums:
        return []

    def f(a, b):
        return str(nums[a]) if a == b else str(nums[a]) + '->' + str(nums[b])
    res = []
    a, b = 0, 0
    for i in range(1, len(nums)):
        # sequence continues
        if nums[i]-1 == nums[i-1]:
            b = i
        # sequence breaks
        else:
            res.append(f(a, b))
            a, b = i, i
    res.append(f(a, b))
    return res