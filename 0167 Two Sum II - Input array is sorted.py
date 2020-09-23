# 双指针
def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i<j:
        if numbers[i]+numbers[j] == target:
            return i+1, j+1
        elif numbers[i]+numbers[j] > target:
            j-=1
        else:
            i+=1

# 哈希表
def twoSum(numbers, target):
    dic = {}
    for i in range(len(numbers)):
        if target - numbers[i] in dic:
            return [dic[target - numbers[i]] + 1, i+1]
        else:
            dic[numbers[i]] = i

print(twoSum([5,25,75],100))