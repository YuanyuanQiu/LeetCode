def divide(dividend, divisor):
    if abs(dividend) < abs(divisor) or dividend ==0:
        return 0
   
    if (dividend > 0 and divisor <0) or (dividend < 0 and divisor > 0):
        flag = -1
    else:
        flag = 1
    
    dividend = abs(dividend)
    divisor = abs(divisor)

    if divisor == 1:
        return max(min(dividend * flag, 2147483647), -2147483648)
    
    n = len(str(divisor))
    s = str(dividend)
    remain = 0
    end = n
    digit = int(s[:end])
    res = ''
    while end <= len(s):
        temp = 0
        # print('s',end, s[:end])
        # print('digit',digit)
        while digit >= divisor:
            temp += 1
            digit -= divisor
        res += str(temp)
        remain = digit
        # print('remain',remain)
        # print('result',res)
        # print('\n')
        
        end += 1
        digit = int(str(remain)+s[end-1:end])
        
    
    return(max(min(int(res)* flag, 2147483647), -2147483648))
                  

print(divide(7,-3))







