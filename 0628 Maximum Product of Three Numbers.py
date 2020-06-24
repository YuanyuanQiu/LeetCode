'''
如果数组中出现了负数，那么我们还需要考虑乘积中包含负数的情况，显然选择最小的两个负数和
最大的一个正数是最优的，即为前两个元素与最后一个元素的乘积
'''

def maximumProduct(nums):
    nums.sort(reverse = True)
    return max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])

print(maximumProduct([1,2,3,4]))