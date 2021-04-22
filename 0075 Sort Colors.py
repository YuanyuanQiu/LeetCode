def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    # 头部元素
    p = 0
    # 交换0，p之前全为0
    for i in range(n):
        if nums[i] == 0:
            nums[i], nums[p] = nums[p], nums[i]
            p += 1
    # 交换1，p之前全为1
    for i in range(ptr, n):
        if nums[i] == 1:
            nums[i], nums[p] = nums[p], nums[i]
            p += 1


def sortColors(self, nums: List[int]) -> None:
    n = len(nums)
    p0 = p1 = 0 # all 0 before p0, all 1 before p1
    for i in range(n):
        if nums[i] == 1:
            nums[i], nums[p1] = nums[p1], nums[i]
            p1 += 1
        elif nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i] # might exchange 1
            if p0 < p1: # already put some 1 ahead
                nums[i], nums[p1] = nums[p1], nums[i]
            p0 += 1
            p1 += 1