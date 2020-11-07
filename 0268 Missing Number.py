def missingNumber(nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number

# 对一个数进行两次完全相同的异或运算会得到原来的数
def missingNumber(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

print(missingNumber([3,0,1]))