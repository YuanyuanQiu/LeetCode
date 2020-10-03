def isPalindrome(s):
    s = s.lower()
    new = ''
    for i in s:
        if i.isalnum():
            new += i

    return new == new[::-1]

