def containsNearbyDuplicate(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic and dic[nums[i]] >= i-k:
            return True
        dic[nums[i]] = i
    return False