def subarraySum(nums, k):
    # 利用 hashmap 记录和的累加值来避免重复计算（累加值:出现次数)
    dic = {}
    dic[0] = 1
    total = count = 0
    for i in range(len(nums)):
        total += nums[i]
        
        if total - k in dic:
            count += dic[total - k]
        
        dic[total] = dic.get(total, 0) + 1
#        print(dic)
    return count

print(subarraySum(nums = [1,2,3,2,1], k = 3))