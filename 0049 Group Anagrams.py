def groupAnagrams(strs):
    dic = {}
    def rank_str(s):
        l = list(s)
        l.sort()
        return ''.join(l)
        
    for i in strs:
        key = rank_str(i)
        dic[key] = dic.get(key,[])
        dic[key].append(i)
        
    return(list(dic.values()))
    
    
    
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
            