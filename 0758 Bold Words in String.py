def boldWords(words, S):
    b = [0]*(len(S)+1)
    
    # 标注所有开头（1）和结尾（-1）
    for w in words:
        begin = 0
        while begin != -1:
            begin = S.find(w,begin)
            if begin != -1:
                # 开头
                b[begin] += 1
                # 结尾
                b[begin + len(w)] -= 1
                begin += 1
    # print(b)
    
    
    rs = '' # answer
    sc = 0 # 指针判断开头结尾，为0则不在括号内
    for i,e in enumerate(b):
        if sc == 0 and e > 0:
            rs += '<b>'
        elif sc > 0 and sc + e == 0:
            rs += '</b>'
        
        if i < len(S):
            rs += S[i]
        sc += e
        
        # print(rs,sc)
    return rs


words = ["ab", "bc"]
S = "aabcd"
print(boldWords(words, S))