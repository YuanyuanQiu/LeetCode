def reverseStr(s, k):
    result = ''
    
    while len(s) > 0:
        if len(s) < k:
            result += s[::-1]
            s = ''
        elif len(s) > 2*k:
            result += s[:k][::-1]
            result += s[k:2*k]
            s = s[2*k:]
        else:
            result += s[:k][::-1]
            result += s[k:]
            s = ''
        # print(result, s)
    return result

print(reverseStr(s = "abcdefg", k = 2))
            
            