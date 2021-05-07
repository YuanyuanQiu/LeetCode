def countPrimes(n):
    is_prime = [True]*(n+1)
    ans = 0
    for num in range(2,n+1):
        if is_prime[num]:
            ans+=1
            for k in range(1,n//num+1):
                is_prime[num*k]=False
    return ans