def findNumberOfLIS(self, nums: List[int]) -> int:
    N = len(nums)
    if N <= 1:
        return N
    lengths = [1] * N #lengths[i] = longest ending in nums[i]
    counts = [1] * N #count[i] = number of longest ending in nums[i]

    for j, num in enumerate(nums):
        for i in range(j): # nums[i] before nums[j]
            if nums[i] < nums[j]: 
                if lengths[i] >= lengths[j]:
                    lengths[j] = 1 + lengths[i]
                    counts[j] = counts[i]
                elif lengths[i] + 1 == lengths[j]:
                    counts[j] += counts[i]

    longest = max(lengths)
    res = 0
    for i, c in enumerate(counts):
        if lengths[i] == longest:
            res += c
    return res