def trap(self, height: List[int]) -> int:
    n = len(height)
    if n <= 2:
        return 0
    left = [0 for _ in range(n)]
    left[0] = height[0]
    right = [0 for _ in range(n)]
    right[-1] = height[-1]
    for i in range(1,n):
        left[i] = max(left[i-1], height[i])
    for j in range(n-2, -1, -1):
        right[j] = max(right[j+1], height[j])
    ans = 0
    for k in range(1,n-1):
        ans += max(min(left[k], right[k]) - height[k], 0)
    return ans