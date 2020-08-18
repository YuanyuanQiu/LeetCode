# def reverseStr(s, k):
#     result = ''
    
#     while len(s) > 0:
#         if len(s) < k:
#             result += s[::-1]
#             s = ''
#         elif len(s) > 2*k:
#             result += s[:k][::-1]
#             result += s[k:2*k]
#             s = s[2*k:]
#         else:
#             result += s[:k][::-1]
#             result += s[k:]
#             s = ''
#         # print(result, s)
#     return result


# def reverseStr(s, k):
#     if len(s) <= k:
#         return s[::-1]

#     ans = ''
#     for i in range(0,len(s),2*k):
#         ans += s[i:i+k][::-1]
        
#         if i+k < len(s):
#             ans += s[i+k:i+2*k]


def reverseStr(s, k):
    a = list(s)
    for i in xrange(0, len(a), 2*k):
        a[i:i+k] = reversed(a[i:i+k])
    return "".join(a)



print(reverseStr(s = "abcdefg", k = 2))
            
            