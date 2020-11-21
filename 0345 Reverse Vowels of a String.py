def reverseVowels(s):
    ls = list(s)
    vowels = 'aeiouAEIOU'
    l, r = 0, len(ls) - 1
    while l < r:
        while ls[l] not in vowels and l < len(ls)-1:
            l += 1
        while ls[r] not in vowels and r > 0:
            r -= 1
        if l < r:
            ls[l], ls[r] = ls[r], ls[l]
        l += 1
        r -= 1
    return ''.join(ls)


# # 双指针，左指针遇到一个元音字母，右指针就从后往前遍历，交换第一个元音字母
# def reverseVowels(s):
#     x={'a','e','i','o','u','A','E','I','O','U'}
#     res=[]
#     j=len(s)-1
#     for i,k in enumerate(s):
#         if k in x:                      
#             while s[j] not in x:
#                 j-=1
#             res.append(s[j])
#             j-=1
#         else:
#             res.append(k)
#     return ''.join(res)


print(reverseVowels("leetcode"))
    