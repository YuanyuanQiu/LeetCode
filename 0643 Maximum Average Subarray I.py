# 滑动窗口+简单剪枝
def findMaxAverage(nums, k: int) -> float:
    ans = numsum = sum(nums[:k])
    for i in range(k,len(nums)):
        numsum += nums[i]-nums[i-k]
        ans = max(ans,numsum)
    return ans/k

print(findMaxAverage([0,1,1,3,3], 4))
    