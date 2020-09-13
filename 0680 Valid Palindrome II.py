def validPalindrome(self, s: str) -> bool:
    def checkPalindrome(s):
        if s[::-1] == s:
            return True
        else:
            return False

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == s[r]: 
            l += 1
            high -= 1
        else:
            return checkPalindrome(s[l+1:r+1]) or checkPalindrome(s[l:r])
    return True