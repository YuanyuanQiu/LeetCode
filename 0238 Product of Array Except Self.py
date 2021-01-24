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
    length = len(nums)
    answer = [0]*length
    
    # answer[i] 表示索引 i 左侧所有元素的乘积
    # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]
    
    # R 为右侧所有元素的乘积
    # 刚开始右边没有元素，所以 R = 1
    R = 1;
    for i in reversed(range(length)):
        # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
        answer[i] = answer[i] * R
        # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
        R *= nums[i]
    
    return answer