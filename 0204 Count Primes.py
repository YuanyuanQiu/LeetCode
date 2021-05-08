def countPrimes(n):
    ls = [True for _ in range(n)]
    count = 0
    for i in range(2,n):
        if ls[i]:
            count += 1
            for j in range(1, (n - 1) // i):
                ls[i + i * j] = False
    return count