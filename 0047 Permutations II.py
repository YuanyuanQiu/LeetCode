def permuteUnique(nums):
    res = []
    nums.sort()
    used = [False for _ in range(len(nums))]   #初始对used的值全部设置为False
    
    def dfs(i,temp_list,used):
        #i：即回溯所到达的第几个元素，用来判断是否回溯到数组最后一个元素了，如果i = 数组长度len(nums)，即为一条完整地路径
        #temp_list:保存回溯过程中的经过的元素（即保存路径），如果i=len(nums)则说明已经是一条完整路径了，则保存到结果数组res
        #used：used数组是用来判断元素在这次回溯过程中是否有被使用过，存在两个状态，used[i]=True说明被使用过，used[i]=False说明未被使用过

        if i == len(nums):
            res.append(temp_list[:])
            return 

        for j in range(len(nums)): 
            if j > 0 and nums[j] == nums[j - 1] and used[j - 1] == True:  
                continue
            if used[j] == False:
                used[j] = True
                dfs(i + 1, temp_list + [nums[j]], used)
                used[j] = False

    dfs(0,[],used)
    
    return res

print(permuteUnique([1,1,2]))