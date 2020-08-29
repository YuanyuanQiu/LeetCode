# def plusOne(digits):
#     n = int(''.join(list(map(str,digits)))) + 1
    
#     ans = []
#     for i in str(n):
#         ans.append(i)
        
#     return ans

def plusOne(digits):
    num_str = ''
    for i in digits:
        num_str += str(i)
    num_str = str(eval(num_str)+1)
    ls = []
    for i in num_str:
        ls.append(eval(i))
    return ls

print(plusOne([1,3,5]))