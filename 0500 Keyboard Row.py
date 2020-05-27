# def findWords(words):
#     row = ['QWERTYUIOPqwertyuiop', 'ASDFGHJKLasdfghjkl', 'ZXCVBNMzxcvbnm']
#     dic = {} # word:level
#     ls = []
    
#     for word in words:
#         flag = False
#         for i in word:
#             for level in row:
#                 if i in level:
#                     dic[word] = dic.get(word,level)
#                     if dic[word] != level:
#                         del dic[word]
#                         flag = True
#                         break
#             if flag:
#                 break
#         else:
#             ls.append(word)
#             del dic[word]
#     return ls

def findWords(words):
    set1 = set('qwertyuiop')
    set2 = set('asdfghjkl')
    set3 = set('zxcvbnm')
    res = []
    for i in words:
        x = i.lower()
        setx = set(x)
        if setx<=set1 or setx<=set2 or setx<=set3:
            res.append(i)
    return res

print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
                        
        
    