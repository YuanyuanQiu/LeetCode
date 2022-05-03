def removeDuplicates(nums):
    f,s = 1,0
    while f < len(nums):
        if nums[f] != nums[s]:
            nums[s+1] = nums[f]
            s += 1
        f += 1
    return len(nums[0:s+1])
        