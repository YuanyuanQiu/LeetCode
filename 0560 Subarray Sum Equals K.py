def subarraySum(nums, k):
    # key为累加值acc，value为累加值acc出现的次数。
    dic = {}
    dic[0] = 1
    total = 0
    res = 0
    for i in range(len(nums)):
        # 迭代数组，然后不断更新 acc 和 hashmap
        total += nums[i]
        if total - k in dic:
            res += dic[total - k]
        dic[total] = dic.get(total, 0) + 1
    return res

print(subarraySum(nums = [1,2,3,2,1], k = 3))