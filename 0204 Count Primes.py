def countPrimes(n):
    is_prime = [True]*n
    ans = 0
    for num in range(2,n):
        if is_prime[num]:
            ans+=1
            for k in range(1,(n - 1)//num+1):
                is_prime[num*k]=False
    return ans