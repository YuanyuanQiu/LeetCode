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
    res = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            cur = num
            cur_count = 1

            while cur + 1 in num_set:
                cur += 1
                cur_count += 1

            res = max(res, cur_count)

    return res