#def longestConsecutive(self, nums: List[int]) -> int:
#    n = len(nums)
#    if n <= 1:
#        return n
#    nums = list(set(nums))
#    nums.sort()
#    dic = {}
#    res = 0
#    for i in nums:
#        if i - 1 in dic:
#            dic[i] = dic[i-1] + 1
#        else:
#            dic[i] = 1
#    return max(dic.values())


def longestConsecutive(self, nums: List[int]) -> int:
    res = 0     # 记录最长连续序列的长度
    num_set = set(nums)     # 记录nums中的所有数值
    for num in num_set:
        # 如果当前的数是一个连续序列的起点，统计这个连续序列的长度
        if (num - 1) not in num_set:
            seq_len = 1     # 连续序列的长度，初始为1
            while (num + 1) in num_set:
                seq_len += 1
                num += 1    # 不断查找连续序列，直到num的下一个数不存在于数组中
            res = max(res, seq_len)     # 更新最长连续序列长度
    return res