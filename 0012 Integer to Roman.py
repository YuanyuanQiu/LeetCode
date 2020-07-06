def intToRoman(num):
    dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M' }
    ls = list(dic.keys())
    ls.sort()
    s = str(num)
    res = ''
    for i in range(len(s)):
        fig = int(s[i])
        num = fig * 10**(len(s) - 1 - i)
        # print('数', fig,num)
        
        if num in dic:
            res += dic[num]
        else:
            for j in range(len(ls)):
                if j == len(ls)-1:
                    res += num//ls[j] * dic[ls[j]]
                    break
                if num > ls[j] and num < ls[j+1]:
                    if fig == 4:
                        res += dic[ls[j]] + dic[ls[j+1]]
                    elif fig == 9:
                        res += dic[ls[j-1]] + dic[ls[j+1]]
                    else:
                        if fig < 5:
                            res += num//ls[j] * dic[ls[j]]
                        else:
                            res += dic[ls[j]] + (num-ls[j])//ls[j-1] * dic[ls[j-1]]
                    break
        # print(res)
    
    return res

# 暴力解法
# def intToRoman(self, num: int) -> str:
#     M = ["", "M", "MM", "MMM"] # 1000，2000，3000
#     C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # 100~900
#     X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # 10~90
#     I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 1~9
#     return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]

# 贪心解
def intToRoman(num):
    hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    res = ''
    for key in hashmap:
        if num // key != 0:
            count = num // key  # 比如输入4000，count 为 4
            res += hashmap[key] * count 
            num %= key
    return res


print(intToRoman(800))
        