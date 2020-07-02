# def convert(s, numRows):
#     if len(s) < numRows:
#         return s
#     # key=row, value=str
#     dic = {}
    
#     ls = list(range(numRows))
#     ls += ls[1:-1][::-1]
    
#     if len(s) > len(ls):
#         ls *= len(s)//len(ls)
#         ls += ls[:len(s)%len(ls)]
    
#     for i in range(len(s)):
#             dic[ls[i]] = dic.get(ls[i],'') + s[i]
    
#     ans = ''
#     for k in range(numRows):
#         ans += dic[k]
    
#     return ans


def convert(s, numRows):
    if numRows < 2: return s
    res = ["" for _ in range(numRows)]

    i, flag = 0, -1
    for c in s:
        res[i] += c
        if i == 0 or i == numRows - 1: 
            flag = -flag
        i += flag
    return "".join(res)


print(convert(s = "PAYPALISHIRING", numRows = 4))