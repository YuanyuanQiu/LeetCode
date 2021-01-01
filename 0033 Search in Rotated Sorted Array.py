class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 有序为[0,mid]
            if nums[0] <= nums[mid]:
                # target 介于[0,mid]
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                # target 介于[mid,n]
                else:
                    l = mid + 1
            # 有序为[mid,n]
            else:
                # target 介于[mid,n]
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                # target 介于[0,mid]
                else:
                    r = mid - 1
        return -1