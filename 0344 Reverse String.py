# def reverseString(s):
#     return s[::-1]

# 双指针遍历半个数组，依次交换各半边对应两个数
def reverseString(s):
    i,j = 0,len(s)-1
    while i<j:
        s[i],s[j] = s[j],s[i]
        i+=1
        j-=1
    return(s)


print(reverseString(["h","e","l","l","o"]))
    