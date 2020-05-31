def checkPerfectNumber(num):
    if num<=1:
        return False
    
    count = 1
    
    for i in range(2,int(num**0.5)+1):
        # print(l,r,count)
        if num % i == 0:
            count += i
            count += num/i
        if count > num:
            return False

    return count == num

print(checkPerfectNumber(28))