def findDuplicate(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 2:
        return nums[0]
    l, r = 0, n - 1
    while l < r:
        mid = l + (r - l) // 2
        cnt = 0
        for i in nums:
            if i <= mid:
                cnt += 1
        # 抽屉原理
        if cnt > mid:
            # 重复的元素一定出现在 [l, mid] 区间里
            r = mid
        else:
            # 重复的元素一定出现在 [mid+1, l] 区间里
            l = mid + 1
    return l