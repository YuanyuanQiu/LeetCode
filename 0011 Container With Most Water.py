# 我们在每一步移动指针时，宽度一定变小（因为 width - 1）
# 若向内移动短板，宽度变小了，高度可能变高，因为原来限制水位的短板变化了，面积可能变大。
# 若向内移动长板，宽度变小了，高度不可能变高，因为限制水位的短板还在原地，面积一定变小。
# 如果两边高度相同，面积已经最大了，移动任意一边都可以。
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        left, right = 0, n-1
        # 
        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            # when to move left
            if height[left] < height[right]:
                left += 1
            # when to move right
            else:
                right -= 1
        return area