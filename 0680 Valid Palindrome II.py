def validPalindrome(self, s: str) -> bool:
    def checkPalindrome(s):
        if s == s[::-1]:
            return True
        else:
            return False
    
    if checkPalindrome(s):
        return True

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return checkPalindrome(s[l+1:r+1]) or checkPalindrome(s[l:r])