def multiply(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    count = 0
    res = 0
    
    for i in range(len(num1)):
        current = ''
        carry = 0
        
        for j in range(len(num2)):
            temp = int(num1[i]) * int(num2[j]) + carry
            current = str(temp)[-1] + current
            if len(str(temp)) > 1:
                carry = int(str(temp)[0])
            else:
                carry = 0
            # print(current)
        res += int(str(carry) + current) * (10**count)
        # print(res)
        count += 1
    
    return str(res)


def multiply(self, num1: str, num2: str) -> str:
    def addStrings(num1, num2):
        # 末尾开始
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry != 0:
            val = (int(num1[i]) if i >= 0 else 0) + (int(num2[j]) if j >= 0 else 0) + carry
            res = [str(val % 10)] + res
            carry = val // 10
            i -= 1
            j -= 1
        return "".join(res)

    if num1 == "0" or num2 == "0":
        return "0"
    
    ans = "0"
    m, n = len(num1), len(num2)
    # 逐个取num2
    for i in range(n - 1, -1, -1):
        carry = 0
        y = int(num2[i])
        res = ["0"] * (n - i - 1) # 补0
        # 逐个取num1
        for j in range(m - 1, -1, -1):
            product = int(num1[j]) * y + carry
            res = [str(product % 10)] + res
            carry = product // 10
        if carry > 0:
            res = [str(carry)] + res
        res = "".join(res)
        ans = addStrings(ans, res)
    
    return ans

print(multiply('123','456'))