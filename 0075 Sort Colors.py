class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return nums
        
        p = 1
        for i in range(n-1):
            p = i + 1
            while p < n:
                if nums[i] > nums[p]:
                    nums[p], nums[i] = nums[i], nums[p]
                p += 1