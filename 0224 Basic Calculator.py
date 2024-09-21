def calculate(self, s: str) -> int:
    # 左边表达式除去栈内保存元素的计算结果，当前遇到的数字，运算符
    res, num, sign = 0, 0, 1
    # 保存遇到左括号时前面计算好了的结果和运算符
    stack = []

    for c in s:
        # 数字：更新num
        if c.isdigit():
            num = 10 * num + int(c)
        # 运算符：更新res，重置num，更新sign
        elif c == "+" or c == "-":
            res += sign * num
            num = 0
            sign = 1 if c == "+" else -1
        # 遇到了右边表达式需优先计算，因此将res和sign进栈为新的开始并重置res和sign
        elif c == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        # 右边表达式结束，把结果出栈并计算整个式子的结果
        elif c == ")":
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()
    
    # 更新最后一个num至res
    res += sign * num
    return res