# def reverseString(s):
#     return s[::-1]

# 双指针遍历半个数组，依次交换各半边对应两个数
def reverseString(s):
    j = len(s)-1
    for i in range(len(s)/2):
        s[i],s[j]=s[j],s[i]
        j -= 1
        i +=1

print(reverseString(["h","e","l","l","o"]))
    