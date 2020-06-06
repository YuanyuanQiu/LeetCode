def reverseWords(s):
    ls = s.split()
    nls = []
    for i in range(len(ls)):
        nls.append(ls[i][::-1])
    return ' '.join(nls)

print(reverseWords("Let's take LeetCode contest"))
        