def lastRemaining(n, m):
    ls = list(range(n))
    
    l = 0
    while len(ls) > 1:
        ind = (l + m - 1) % len(ls)
        l = ind
        del ls[ind]
    
    return ls[0]