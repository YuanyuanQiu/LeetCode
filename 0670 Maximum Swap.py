def maximumSwap(self, num: int) -> int:
    # 先将int转为ls，方便遍历
    ls = list(str(num))
    if len(ls) == 1:
        return num
    
    for i in range(len(ls)-1):
        maxbehind = max(map(int, ls[i+1:]))
        if maxbehind > int(ls[i]):
            for j in range(len(ls) - 1, -1, -1):
                if int(ls[j]) == maxbehind:
                    ls[i], ls[j] = ls[j], ls[i]
                    return int(''.join(ls))
    return num