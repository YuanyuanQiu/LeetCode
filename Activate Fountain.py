# Greedy + Two Pointers
def activateFountains(A):
    if not A: return 0
    # left end -> right end
    n = len(A)
    aux = [0]*(n+1)
    for i, x in enumerate(A, 1):
        aux[max(i - x, 1)] = max(aux[max(i-x,1)], min(i + x, n))
        # print(max(i - x, 1), min(i + x, n))
        # print(aux[1:])

    ans, l, r = 0, 1, aux[1]
    while r <= n:
        ans += 1
        l = r + 1
        if l > n:
            break
        r = aux[l]
    return ans
print(activateFountains([2,0,2,0,0]))