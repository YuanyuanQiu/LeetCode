def findSubstring(self, s: str, words: List[str]) -> List[int]:
    res = []
    # s划分为m节，每节n长度，可能剩余不足n个字母（0~n)
    m, n, ls = len(words), len(words[0]), len(s)
    # 对s有n种划分方式，即先删去前i（i=0∼n−1）个字母后，将剩下的字母进行划分
    for i in range(n):
        # 如果剩余s部分不够涵盖所有words，跳出循环
        if i + m * n > ls:
            break
        
        # 创建新的空计数器
        differ = Counter()
        # 遍历每一节s来更新计数器
        for j in range(m):
            # 每一节s对应的word
            word = s[i+j*n : i+(j+1)*n]
            # 出现在s，计数器加1
            differ[word] += 1
        # 遍历words来更新计数器，当前窗口内多哪些？少哪些？
        for word in words:
            # 出现在words，计数器减1
            differ[word] -= 1
            if differ[word] == 0:
                del differ[word]
        
        # 窗口右移，间隔为词长n，右边进长为n的单词，左边出长为n的单词
        for start in range(i, ls-m*n+1, n):
            # start为i时不需要移动，直接判断
            # start不为i时需要移动
            if start != i:
                # 窗口右边要加哪个单词，维护词频差
                word = s[start+(m-1)*n: start+m*n]
                differ[word] += 1
                if differ[word] == 0:
                    del differ[word]

                # 窗口左边要减哪个单词，维护词频差
                word = s[start-n:start]
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]

            # 判断，词频差为0表示满足要求
            if len(differ) == 0:
                res.append(start)
    
    return res