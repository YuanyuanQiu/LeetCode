def longestCommonPrefix(strs):
    s=''
    for i in zip(*strs): #将对象中对应元素打包成元组，返回元组组成的列表。
        if len(set(i)) == 1: #元组内所有元素相同
            s += i[0]
        else:
            break
    return s

print(longestCommonPrefix(["flower","flow","flight"]))