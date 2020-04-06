# def missingNumber(nums):
#     n = max(nums)
#     nums_all=list(range(n+1))
#     for i in nums:
#         nums_all.remove(i)
#     if nums_all == []:
#         return n+1
#     else:
#         return nums_all[0]

def missingNumber(nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number

print(missingNumber([3,0,1]))