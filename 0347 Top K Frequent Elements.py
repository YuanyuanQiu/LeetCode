# hashtable + sort
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n == 1:
        return nums
    if len(set(nums)) <= k:
        return list(set(nums))
    dic = {}
    for i in nums:
        dic[i] = dic.get(i,0) + 1
    return sorted(list(dic.keys()), key=lambda x: dic[x], reverse=True)[:k]