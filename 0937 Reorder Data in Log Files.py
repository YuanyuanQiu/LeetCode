def reorderLogFiles(logs):
    dic_letter = []
    dic_digit = []
    
    for i in logs:
        temp = i.split(' ')
        if ''.join(temp[1:]).isalpha():
            dic_letter.append(i)
        else:
            dic_digit.append(i)
    
    dic_letter.sort(key=lambda x: (' '.join(x.split(' ')[1:]), x.split(' ')[0]))
    return dic_letter+dic_digit


print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))