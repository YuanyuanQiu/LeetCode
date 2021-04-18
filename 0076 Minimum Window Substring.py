def minWindow(self, s: str, t: str) -> str:
    need = collections.defaultdict(int)
    for c in t:
        need[c] += 1
    needCnt = len(t)
    i = 0 #记录起始位置
    res = (0, float('inf'))  #用两个元素，方便之后记录起终点
    #三步骤：
    #1. 增加右边界使滑窗包含t
    for j,c in enumerate(s):
        if need[c] >0:
            needCnt -= 1
        need[c] -= 1 #这行放在外面不可以，看19行 need[c] == 0
    #2. 收缩左边界直到无法再去掉元素   !注意，处理的是i
        if needCnt == 0:
            while True:
                c = s[i]
                if need[c] == 0: #表示再去掉就不行了(need>0)
                    break
                else:
                    need[c] += 1
                    i += 1
            if j-i < res[1] - res[0]:  #这里是否减一都可以，只要每次都是这样算的就行，反正最后也是输出子串而非长度
                res = (i,j)
    #3. i多增加一个位置，准备开始下一次循环(注意这步是在 needCnt == 0里面进行的 )
            need[s[i]] += 1
            needCnt += 1    #由于 移动前i这个位置 一定是所需的字母，因此NeedCnt才需要+1
            i += 1
    return "" if res[1]>len(s) else s[res[0]: res[1]+1]