# 字典
def majorityElement(nums):
    n = len(nums)
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]=0
        dic[i]+=1
        if dic[i]>n/2:
            return i


# 一个随机的下标很有可能存有众数
import random

def majorityElement(nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


# 摩尔投票法（Boyer–Moore majority vote algorithm），也被称作「多数投票法」
'''
算法可以分为两个阶段：
对抗阶段：分属两个候选人的票数进行两两对抗抵消
计数阶段：计算对抗结果中最后留下的候选人票数是否有效
'''
def majorityElement(self, nums):
    major = 0
    count = 0
    
    for n in nums:
        if count == 0:
            major = n
        if n == major:
            count = count + 1
        else:
            count = count - 1

    return major


print(majorityElement([3,2,3]))