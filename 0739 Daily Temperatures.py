def dailyTemperatures(self, T: List[int]) -> List[int]:
    n = len(T)
    if n < 2:
        return 0
    ans = [0] * n
    # 栈存放所在日，若当日比栈尾温度高，栈尾日结果update为当日与栈尾所在日之差并从栈中移除
    stack = []
    for i in range(n):
        # 结束条件为全部移除或没有出现更高的温度
        while stack and T[i] > T[stack[-1]]:
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index
        stack.append(i)
    return ans