def reorderLogFiles(logs):
    letter = []
    digit = []
    for i in logs:
        content = i.split()[1]
        if content.isalpha():
            letter.append(i)
        else:
            digit.append(i)
    letter = sorted(letter, key=lambda x: (x.split()[1:], x.split()[0]))
    return letter + digit


print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))