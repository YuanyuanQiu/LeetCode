#def productExceptSelf(self, nums: List[int]) -> List[int]:
#    n = len(nums)
#    zeros = nums.count(0)
#
#    if zeros > 1:
#        return [0] * n
#            
#    product = 1
#    for num in nums:
#        if num != 0:
#            product *= num
#    
#    if zeros == 1:
#        res = [0] * n
#        idx = nums.index(0)
#        res[idx] = product
#        return res
#
#    res = []
#    for i in range(n):
#        res.append(int(product/nums[i]))
#                  
#    return res

def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    # product till nums[i-1] left to right
    dp = [1] * n
    for i in range(1, n):
        dp[i] = dp[i-1] * nums[i-1] 
    
    # product till nums[i+1] right to left
    R = 1
    for i in range(n-1, -1, -1):
        dp[i] = dp[i] * R
        R *= nums[i]
    return dp