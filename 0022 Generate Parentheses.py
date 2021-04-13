# backtrack
def generateParenthesis(self, n: int) -> List[str]:
    s = '(' * n + ')' * n
    res = []
    def backtrack(history, remain):
        if not remain:
            res.append(history)
        for i in range(len(remain)):
            if i > 0 and remain[i] == remain[i-1]:
                continue
            if not history:
                if remain[i] == ')':
                    continue
                else:
                    backtrack(history + remain[i], remain[:i] + remain[i+1:])
            elif history[-1] == '(' or remain[i] == '(':
                backtrack(history + remain[i], remain[:i] + remain[i+1:])
            else:
                left = history.count('(')
                right = history.count(')')
                if right < left:
                    backtrack(history + remain[i], remain[:i] + remain[i+1:])
                else:
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