def isPalindrome(s):
    s = s.lower()
    new = ''
    for i in s:
        if i.isalnum():
            new += i

    return new == new[::-1]

def isPalindrome(self, s: str) -> bool:
    n = len(s)
    left, right = 0, n - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right:
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1

    return True