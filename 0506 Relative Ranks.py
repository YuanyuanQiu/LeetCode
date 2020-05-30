def findRelativeRanks(nums):
    N = len(nums)
    if N == 0:
        return nums
    
    sort = sorted(nums, reverse = True)
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    for i in range(N):
        rank = sort.index(nums[i])
        if rank <3:
            nums[i] = medals[rank]
        else:
            nums[i] = str(rank+1)
    
    return nums

print(findRelativeRanks([10,3,8,9,4]))
        
    
    
    
    
    