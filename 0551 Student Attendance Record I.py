# def checkRecord(s):
#     if s.count('A')>1:
#         return False
#     if 'LLL' in s:
#         return False
#     return True

def checkRecord(s):
    return not(len(s.split('A'))>2 or "LLL" in s)

print(checkRecord("PPALLL"))