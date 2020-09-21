def isValid(s: str) -> bool:
    '''
    字典：key=左括号, value=右括号
    栈：遍历每个元素，若左放入字符串，若右则匹配字符串最后一个是否登对，是则去掉,
    否则False    
    '''    
    if s == '':
        return True
    
    if len(s)%2 !=0:
        return False
    
    dict1={'(':')','{':'}','[':']'}
    
    ls = [] # 只存左括号
    for i in s:
        # 左括号
        if i in dict1.keys():
            ls.append(i)
        # 右括号
        else:
            if ls == [] or dict1[ls[-1]] != i:
                return False
            else:
                del ls[-1]
    
    return ls == []


print(isValid("){"))
            
    