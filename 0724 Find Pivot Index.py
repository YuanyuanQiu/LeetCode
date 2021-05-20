def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == (total - left - x):
            return i
        left += x
    return -1

print(pivotIndex([-1,-1,-1,-1,-1,0]))