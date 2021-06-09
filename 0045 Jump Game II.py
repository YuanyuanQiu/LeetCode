def jump(self, nums: List[int]) -> int:
    n = len(nums)
    # 当前能够到达的最大下标位置，边界，次数
    maxPos, end, step = 0, 0, 0
    # 在访问最后一个元素之前，我们的边界一定大于等于最后一个位置
    for i in range(n - 1):
        if maxPos >= i:
            maxPos = max(maxPos, i + nums[i])
            # 到达边界时，更新边界并将跳跃次数增加 1
            if i == end:
                end = maxPos
                step += 1
    return step