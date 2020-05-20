# def findContentChildren(g, s):
#     g.sort(reverse = True)
#     s.sort(reverse = True)
#     count = 0
#     for i in range(len(s)):
#         for j in range(len(g)):
#             if s[i] >= g[j]:
#                 count += 1
#                 del g[j]
#                 break
#     return count

def findContentChildren(g, s):
    # 从小到大排序
    g.sort()
    s.sort()
    if len(s)==0 or len(g)==0 or s[-1]<g[0]:return 0
    
    gi=si=count=0
    # 双指针
    while gi<len(g) and si<len(s):
        if s[si]>=g[gi]:
            count+=1
            s[si]=0
            # gi有条件移动
            gi+=1
        # si 必定移动
        si+=1
    return count

print(findContentChildren([1,2,3], [1,1]))