def findMin(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    mid = n // 2
    left = nums[:mid]
    right = nums[mid:]
    left_min = self.findMin(left)
    right_min = self.findMin(right)
    return min(left_min, right_min)