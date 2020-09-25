def pivotIndex(nums):
    S = sum(nums)
    leftsum = 0
    for i, x in enumerate(nums):
        if leftsum == (S - leftsum - x):
            return i
        leftsum += x
    return -1

print(pivotIndex([-1,-1,-1,-1,-1,0]))