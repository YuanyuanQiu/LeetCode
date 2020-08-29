# def strStr(self, haystack: str, needle: str) -> int:
#     if needle == '':
#         return 0
#     ls = haystack.split(needle)
#     if len(ls) == 1:
#         return -1
#     else:
#         return len(ls[0])

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

print(strStr('hello',''))