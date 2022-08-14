def minSubsequence(nums):
    nums.sort(reverse=True)
    tot, s = sum(nums), 0
    for i, num in enumerate(nums):
        s += num
        if s > tot - s:
            return nums[:i+1]