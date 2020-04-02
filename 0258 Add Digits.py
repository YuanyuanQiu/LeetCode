# def addDigits(num):
#     if len(str(num)) < =1:
#         return num
#     while len(str(num)) > 1:
#         count = 0
#         for i in str(num):
#             count += eval(i)
#             num = count
#     return num

def addDigits(num):
    while num >= 10: # 两位数以上
        sum = 0
        while num > 0:
            sum += num % 10 # 取最后一位数
            num //= 10 # 去掉最后一位
        num = sum
    return num


print(addDigits(38))
            
        