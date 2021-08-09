def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    ls = sorted(nums)
    ans = []
    for i in nums:
        ans.append(ls.index(i))
    return ans