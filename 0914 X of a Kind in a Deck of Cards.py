# # 暴力法
def hasGroupsSizeX(deck):
    dic = {}
    for i in deck:
        dic[i] = dic.get(i,0) + 1

    n = len(deck)
    for i in range(2, n+1):
        # i是否为n的约数
        if n % i == 0:
            # i是否为每一个GROUP的约数
            if all(v % i == 0 for v in dic.values()):
                return True
    return False