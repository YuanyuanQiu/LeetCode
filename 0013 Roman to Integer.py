# def romanToInt(s: str) -> int:
#         Roman_single={}
#         Roman_single["I"]=1
#         Roman_single["V"]=5
#         Roman_single["X"]=10
#         Roman_single["L"]=50
#         Roman_single["C"]=100
#         Roman_single["D"]=500
#         Roman_single["M"]=1000

#         Roman_combined={}
#         Roman_combined["IV"]=4
#         Roman_combined["IX"]=9
#         Roman_combined["XL"]=40
#         Roman_combined["XC"]=90
#         Roman_combined["CD"]=400
#         Roman_combined["CM"]=900

#         num=0

#         for i in Roman_combined.keys(): #先剔除掉两位的并求和
#             if i in s:
#                 s=s.replace(i,'')
#                 num+=Roman_combined[i]
#         for j in s: #剩余字符求和
#                 num+=Roman_single[j]
#         return num


def romanToInt(s: str) -> int:
    if len(s) == 0:
        return 0
    
    dic = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 
        'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
    
    if len(s) == 1:
        return dic[s]
    
    ans = 0
    i = 0
    while i+1 <= len(s):
        if s[i:i+2] in dic:
            ans += dic[s[i:i+2]]
            i += 2
        else:
            ans += dic[s[i:i+1]]
            i += 1
    
    return ans

print(romanToInt("MCMXCIV"))