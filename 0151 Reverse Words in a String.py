def reverseWords(self, s: str) -> str:
    ls = s.strip().split()
    ls = ls[::-1]
    return ' '.join(ls)