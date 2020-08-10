def numPairsDivisibleBy60(time):
	# 字典用来统计余数及出现次数
    dic={}
    for i,t in enumerate(time):
        r = t % 60
        dic[r] = dic.get(r,0) + 1

    count = 0
    # 遍历 0 到 30，通过 60-i 便可拿到整除 60 后所有余数可能
    for i in range(31):
    	# 如果余数为 0  或 30，单独处理
        if i in [0,30]:
            num = dic.get(i)
            if num and num>1:
                count+=num*(num-1)//2 # (num-1)+(num-2)+...+1
        # 正常组合为 60 的余数组，取到互配的余数个数，计算结果
        else:
            num1 = dic.get(i)
            num2 = dic.get(60-i)
            if num1 and num2:                  
                count += num1 * num2
    return count

print(numPairsDivisibleBy60([30,20,150,100,40]))