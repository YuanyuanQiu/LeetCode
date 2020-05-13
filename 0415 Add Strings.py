def addStrings(num1, num2):
    res = ""
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    while i >= 0 or j >= 0:
        # 尾部数字
        n1 = int(num1[i]) if i >= 0 else 0 # 长度较短的数字前面填0
        n2 = int(num2[j]) if j >= 0 else 0 # 长度较短的数字前面填0
        tmp = n1 + n2 + carry
        # 进位
        carry = tmp // 10
        # 结果
        res = str(tmp % 10) + res
        # 往前移一位
        i, j = i - 1, j - 1
    return "1" + res if carry else res

print(addStrings('51189', '967895'))