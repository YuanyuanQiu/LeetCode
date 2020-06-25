# def findErrorNums(nums):
#     ls = []
#     dic = {}
#     for i in range(len(nums)):
#         dic[nums[i]] = dic.get(nums[i],0)+1
#         if dic[nums[i]] > 1:
#             ls.append(nums[i])
#             nums.remove(nums[i])
#             break
#     nums.sort()
#     if len(nums) == nums[-1]:
#         ls.append(nums[-1]+1)
#     else:
#         ls.append(int((nums[-1]*(1+nums[-1]))/2-sum(nums[:])))
#     return ls


def findErrorNums(nums):
    # 求差集
    true = [i for i in range(1, len(nums)+1)]
    res = list(set(nums) ^ set(true))
    b = res[0]
    
    # 两个集合一块做^, 得到a ^ b的结果c， 已知b，c, 可以得到c ^ b = a
    # a ^ b = c --> c ^ b = a
    c = 0
    for n in nums:
        c ^= n # 任何数和0异或是本身
    for i in range(1, len(nums)+1):
        c ^= i
    a = b^c  
    return [a, b]


print(findErrorNums([1,2,2,4]))



