def largestPerimeter(self, nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0
    nums.sort(reverse=True)
    for i in range(n-2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0