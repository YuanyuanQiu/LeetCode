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
    if num == 0:
        return 0

    if num % 9 == 0:
        return 9
    
    # F(N) = N - 9xM, M = (M1+M2+M3+...)
    return num % 9

print(addDigits(38))