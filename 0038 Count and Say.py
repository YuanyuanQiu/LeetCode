# 双指针
def countAndSay(n):
    res = ["1",]  # 当前输出外观res数列
    r = 1
    while r < n: # 一直算到要求的第n行为止
        r += 1
        p, q = 0, 1 # p初始化为0，q初始化为1，遍历当前输出外观res以获得下一输出；
        tmp = []    # 下一行输出外观数列
        while q <= len(res):
            if q == len(res): # 特殊边界位置的处理：当q == len(res)刚好溢出时
                # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
                tmp.extend([str(q-p), res[p]]) 
            elif res[p] != res[q]:
                tmp.extend([str(q-p), res[p]])
                p = q  # p指向下一个不同的数字即让p=q，q重复上述2.
            q += 1     
        res =  tmp   # 节省空间，利用上一行计算下一行，故直接用计算出的当前行替换上一行
    return "".join(res)

# 递归
def countAndSay(n):
    if n == 1:
        return '1'
    
    last = self.countAndSay(n-1)
    ans = ''
    l = 0
    r = l + 1
    while r < len(last):
        if last[r] == last[l]:
            r += 1
        else:
            ans += str(r-l) + last[l]
            l = r
            r = l + 1
    ans += str(r-l) + last[l]

    return ans

print(countAndSay(5))
