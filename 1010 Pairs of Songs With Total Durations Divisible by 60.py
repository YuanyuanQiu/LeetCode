def numPairsDivisibleBy60(time):
	# 字典用来统计余数及出现次数
    dic={}
    for i,t in enumerate(time):
        r = t % 60
        dic[r] = dic.get(r,0) + 1
    
    '''
    拿到所有余数后，其范围是 0 到 59。假设余数为 1 的有 10 个，余数为 59 的有 5 个，
    那么我们可以算出它们可以生成 10*5 = 50 对有效结果；但这里特殊的是余数为 0 和 30 
    的，假设余数为 30 的数字有 10 个，那么产生的不重复有效结果为 10 * 9/2 = 45 对。

    '''
    count = 0
    # 遍历 0 到 30，通过 60-i 便可拿到整除 60 后所有余数可能
    for i in range(31):
    	# 如果余数为 0或 30，单独处理
        if i in [0,30]:
            num = dic.get(i)
            if num and num>1:
                count += num*(num-1)//2 # (num-1)+(num-2)+...+1
        
        # 正常组合为 60 的余数组，取到互配的余数个数，计算结果
        else:
            num1 = dic.get(i)
            num2 = dic.get(60-i)
            if num1 and num2:                  
                count += num1 * num2
    return count

print(numPairsDivisibleBy60([30,20,150,100,40]))