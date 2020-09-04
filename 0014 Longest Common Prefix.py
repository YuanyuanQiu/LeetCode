# def longestCommonPrefix(strs):
#     s=''
#     for i in zip(*strs): #将对象中对应元素打包成元组，返回元组组成的列表。
#         if len(set(i)) == 1: #元组内所有元素相同
#             s += i[0]
#         else:
#             break
#     return s

'''
 string 比较采用的是 ”字典序“，即比较当前字符大小，若当前字符小则此字符串较小，
 若相等则继续往后比较，直到某一字符不相等或某一字符串比较结束，比较结束都相等，
 则长度小的字符串较小。
 a,bc,aac,第一个字符分别是 a,b,a, 则第二个字符串bc最大，
 a 小于 aac 所以最小字符串为 a,最大字符串为 bc,则其公共前缀为 "",没有相等的，为空
 '''

# 先找出数组中字典序最小和最大的字符串，最长公共前缀即为这两个字符串的公共前缀
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    str0 = min(strs)
    str1 = max(strs)
    
    for i in range(len(str0)):
        if str0[i] != str1[i]:
            return str0[:i]
    return str0


print(longestCommonPrefix(["flower","flow","flight"]))