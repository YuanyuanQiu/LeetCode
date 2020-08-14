# def reverseVowels(s):
#     s = list(s)
#     vowels = ['a','e','i','o','u','A','E','I','O','U']
    
#     l = 0
#     r = len(s) - 1
    
#     while l < r:
#         while s[l] not in vowels and l < len(s) - 1:
#             l += 1
#         if l == len(s) - 1:
#             return ''.join(s)
        
#         while s[r] not in vowels and r > 0:
#             r -= 1
        
#         if l < r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1

#     return ''.join(s)


# 双指针，左指针遇到一个元音字母，右指针就从后往前遍历，交换第一个元音字母
def reverseVowels(s):
    x={'a','e','i','o','u','A','E','I','O','U'}
    res=[]
    j=len(s)-1
    for i,k in enumerate(s):
        if k in x:                      
            while s[j] not in x:
                j-=1
            res.append(s[j])
            j-=1
        else:
            res.append(k)
    return ''.join(res)


print(reverseVowels("leetcode"))
    