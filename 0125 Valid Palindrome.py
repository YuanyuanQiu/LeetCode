def isPalindrome(s):
    s = s.lower()
    new = ''
    for i in s:
        if i.isalnum():
            new += i
    # print(new)
    return new == new[::-1]


def isPalindrome(s):
    if len(s)<2:
        return True
    else:
        for i in s:
            if i.isalnum()==False:
                s=s.replace(i,'')
        if s.lower()==s.lower()[::-1]:
            return True
        else:
            return False