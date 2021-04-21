def removeKdigits(self, num: str, k: int) -> str:
    n = len(num)
    if n <= k:
        return '0'
    stack = ''
    for i in range(n):
        while k and stack and int(num[i]) < int(stack[-1]):
            stack = stack[:-1]
            k -= 1
        stack += num[i]
    # k > 0单调递增，去掉末尾k个数字
    if k:
        res = stack[:-k]
    else:
        res = stack
    return res.lstrip('0') or '0'