# fast-slow pointer 
def removeElement(nums, val):
    f,s = 0,0

    while f < len(nums):
        if nums[f] != val:
            nums[s] = nums[f]
            s += 1
        f += 1

    return s


def removeElement(nums, val):
    for i in nums[:]:
        if i == val:
            nums.remove(val)
    return len(nums)


 print(removeElement([3,2,2,3], 3))