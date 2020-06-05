def findPairs(nums, k):
    if k < 0:
        return 0
    if k == 0:
        return len(set([i for i in nums if nums.count(i)>=2]))
    cl = [i+k for i in nums]
    return len(set(cl) & set(nums))

print(findPairs([-1,-2,-3], 1))