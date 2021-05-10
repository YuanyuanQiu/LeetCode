# backtrack
def generateParenthesis(self, n: int) -> List[str]:
    s = '(' * n + ')' * n
    res = []
    def backtrack(history, remain):
        if not remain:
            res.append(history)
        for i in range(len(remain)):
            if i > 0 and remain[i] == remain[i-1]: # 跳过重复
                continue
            # 第一个必须为'('
            if not history: 
                if remain[i] == ')':
                    continue
                else:
                    backtrack(history + remain[i], remain[:i] + remain[i+1:])
            # history末尾为'('或remain[i]为'('
            elif history[-1] == '(' or remain[i] == '(':
                backtrack(history + remain[i], remain[:i] + remain[i+1:])
            # history末尾为')'且remain[i]为')'
            else:
                left = history.count('(')
                right = history.count(')')
                if right < left: # 右括号少于左括号，可继续添加
                    backtrack(history + remain[i], remain[:i] + remain[i+1:])
                else: # 右括号等于左括号，不可继续
                    continue
    backtrack('',s)
    return res


# recursion
# (left)right
def generateParenthesis(n):
    if n == 0:
        return ['']
    ans = []
    for c in range(n):
        for left in self.generateParenthesis(c):
            for right in self.generateParenthesis(n-1-c):
                ans.append('({}){}'.format(left, right))
    return ans

        
print(generateParenthesis(3))