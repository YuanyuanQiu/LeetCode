# def addStrings(num1, num2):
#     res = ""
#     i, j, carry = len(num1) - 1, len(num2) - 1, 0
#     while i >= 0 or j >= 0:
#         # 从尾到头
#         n1 = int(num1[i]) if i >= 0 else 0 # 长度较短的数字前面填0
#         n2 = int(num2[j]) if j >= 0 else 0 # 长度较短的数字前面填0
#         tmp = n1 + n2 + carry
#         # 进位
#         carry = tmp // 10
#         # 结果
#         res = str(tmp % 10) + res
#         # 往前移一位
#         i, j = i - 1, j - 1
#     return "1" + res if carry else res


def addStrings(num1, num2):
    s1 = list(num1)[::-1]
    s2 = list(num2)[::-1]

    carry = 0 # 进位
    res = []
    i = 0
    while i < len(s1) or i < len(s2) or carry:
        n1 = int(s1[i]) if i < len(s1) else 0
        n2 = int(s2[i]) if i < len(s2) else 0
        
        carry, n = divmod(n1 + n2 + carry, 10)
        res.append(str(n))
        i += 1
    return ''.join(res[::-1])


print(addStrings('51189', '967895'))