def threeSum(nums):
    n=len(nums)
    res=[]
    
    # 特判
    if(not nums or n<3):
        return []
    
    # 排序
    nums.sort()
    
    # 遍历
    res=[]
    for i in range(n):
        # 若>0: 因为已排序好，后面不可能有3个数和为0，直接返回结果
        if(nums[i]>0):
            return res
        
        # 跳过重复元素避免重复解
        if(i>0 and nums[i]==nums[i-1]):
            continue
        
        # 双指针
        L=i+1
        R=n-1
        while(L<R):
            if(nums[i]+nums[L]+nums[R]==0):
                res.append([nums[i],nums[L],nums[R]])
                # 跳过重复元素
                while(L<R and nums[L]==nums[L+1]):
                    L=L+1
                while(L<R and nums[R]==nums[R-1]):
                    R=R-1
                L=L+1
                R=R-1
            elif(nums[i]+nums[L]+nums[R]>0):
                R=R-1
            else:
                L=L+1
    return res
