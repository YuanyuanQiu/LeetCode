def multiply(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    count = 0
    res = 0
    
    for i in range(len(num1)):
        current = ''
        forward = 0
        
        for j in range(len(num2)):
            temp = int(num1[i]) * int(num2[j]) + forward
            current = str(temp)[-1] + current
            if len(str(temp)) > 1:
                forward = int(str(temp)[0])
            else:
                forward = 0
            # print(current)
        res += int(str(forward) + current) * (10**count)
        # print(res)
        count += 1
    
    return str(res)

print(multiply('123','456'))