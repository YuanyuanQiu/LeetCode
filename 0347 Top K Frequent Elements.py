# hashtable + sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        dic = {}
        for i in range(n):
            dic[nums[i]] = dic.get(nums[i],0) + 1
        
        a = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(a[i][0])
        return ans