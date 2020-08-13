# def longestCommonPrefix(strs):
#     s=''
#     for i in zip(*strs): #将对象中对应元素打包成元组，返回元组组成的列表。
#         if len(set(i)) == 1: #元组内所有元素相同
#             s += i[0]
#         else:
#             break
#     return s

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