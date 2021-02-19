def titleToNumber(s):
    ans = 0
    for i in s:
        ans = ans * 26 + ord(i) - ord('A') + 1
    return ans

print(titleToNumber('AA'))
        