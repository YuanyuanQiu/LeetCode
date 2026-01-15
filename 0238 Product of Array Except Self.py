# Option 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1] * n
        R = [1] * n
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1] # 左边所有数字乘积
        for j in range(n-2, -1, -1):
            R[j] = R[j+1] * nums[j+1] # 右边所有数字乘积
        return list(map(lambda x, y: x * y, L, R ))

# Option 2 优化版O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        
        # 1. 先计算左侧乘积，直接存入 answer
        # L[i] = L[i-1] * nums[i-1]
        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        # 2. 动态计算右侧乘积，并直接乘到 answer 上
        # 我们不需要一个数组存 R，只需要一个变量 R_accumulation
        R = 1
        for i in range(n - 1, -1, -1):
            # answer[i] 已经是左边的积了，现在乘上右边的积
            answer[i] = answer[i] * R
            # 更新右边的累积积，为下一个位置（i-1）做准备
            R = R * nums[i]
            
        return answer