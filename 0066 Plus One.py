# 投机取巧法
def plusOne(digits):
    num_str = ''
    for i in digits:
        num_str += str(i)
    num_str = str(eval(num_str)+1)
    ls = []
    for i in num_str:
        ls.append(eval(i))
    return ls


# 正常解法 从后往前依次判断末尾是否为9 如果是 则去除：
def plusOne(digits):
    newlst = []
    while digits and digits[-1] == 9:
        digits.pop()
        newlst.append(0)
    if not digits:
        return [1] + newlst
    else:
        digits[-1] += 1
        return digits + newlst
    

# Math
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        n = len(digits)
        s = 0
        l = 0
        res = []
        while l < n or s:
            if l < n:
                s += digits[l]
            if l == 0:
                s += 1
            res.append(s % 10)
            s = s // 10
            l += 1
        return res[::-1]

print(plusOne([1]))