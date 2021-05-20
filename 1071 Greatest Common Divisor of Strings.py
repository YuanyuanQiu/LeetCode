def gcdOfStrings(str1, str2):
    if set(str1) != set(str2):
        return ''
    n1, n2 = len(str1), len(str2)
    if n1 < n2:
        str1, str2 = str2, str1
        n1, n2 = n2, n1
    a, b = n1, n2
    r = a % b
    while r:
        a, b = b, r
        r = a % b
    for i in range(b, 0, -1):
        if n1 % i == 0 and n2 % i == 0 and str1[:i] * (n1 // i) == str1 and str2[:i] * (n2 // i) == str2:
            return str1[:i]
    return ''