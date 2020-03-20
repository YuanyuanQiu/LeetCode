'''
同构代表两个字符串中每个位置上字符在自身第一次出现的索引相同
'''

def isIsomorphic(s, t):
    return [*map(s.index, s)] == [*map(t.index, t)]

print(isIsomorphic("abab","baba"))
        