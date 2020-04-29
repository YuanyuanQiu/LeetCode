import collections
def findTheDifference(s, t):
    # dic = {}
    # for i in t:
    #     if i not in s:
    #         return i
    #     dic[i] = dic.get(i,0)+1
    #     if s.count(i) < dic[i]:
    #         return i
    return list((collections.Counter(t)-collections.Counter(s)).elements())[0]

print(findTheDifference("abcd","abcde"))