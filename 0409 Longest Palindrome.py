def longestPalindrome(s):
    dic = {}
    count = 0
    for i in s:
        dic[i] = dic.get(i,0)+1
        if dic[i] == 2:
            del dic[i]
            count +=1
    if dic != {}:
        return count*2+1
    else:
        return count*2

print(longestPalindrome("abccccdd"))