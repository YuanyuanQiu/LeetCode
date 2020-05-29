def convertToBase7(num):
    sign = False
    rs = []
    if num // 7 == 0:
        return str(num)
    if num<0:
        sign = True
        num = abs(num)
    while num != 0:
        q = num//7
        r = num % 7
        rs.append(str(r))
        num = q
    if sign == True:
        return '-'+''.join(rs[::-1])
    else:
        return ''.join(rs[::-1])

print(convertToBase7(-7))