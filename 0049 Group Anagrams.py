def groupAnagrams(strs):
    if len(strs) <= 1:
        return [strs]
    dic = {}
    for i in strs:
        key = ''.join(sorted(i))
        dic[key] = dic.get(key,[]) + [i]
    return list(dic.values())