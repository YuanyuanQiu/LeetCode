def checkPossibility(nums):
    count = 0
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            count += 1
            # 不越界
            # 特殊情况提前结束：同时不满足
            # 1. nums[i]后面的数不能比nums[i-1]小
            # 2. nums[i-1]前面的数不能比nums[i]大
            if i+1 < len(nums) and i-2 >= 0:
                if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]:
                    return False
        if count > 1:
            return False
    return True

print(checkPossibility([3,4,1,2]))