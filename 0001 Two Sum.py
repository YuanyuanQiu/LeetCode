# # 暴力法
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         if target - nums[i] in nums[i+1:]:
#             return [i, nums[i+1:].index(target - nums[i])+i+1]

# # target=num1+num2 --> num1=target-num2
# def twoSum(nums, target):
#     hashmap={} # 定义空字典
#     for ind,num in enumerate(nums): #enumerate函数结果(index,列表元素)
#         hashmap[num] = ind # 遍历存储{列表元素：index}
#     for i,num in enumerate(nums):
#         j = hashmap.get(target - num) # 获得num1与num2
#         if j is not None and i!=j: # num1与num2需不相同
#             return [i,j]

# 遍历列表同时查字典
def twoSum(nums, target):
    dct = {}
    for i, n in enumerate(nums):
        if target - n in dct:
            return [dct[target - n], i]
        dct[n] = i

print(twoSum(nums=[2, 7, 11, 15],target=9))
