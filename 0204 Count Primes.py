# 要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数。

def countPrimes(n):
    # 最小的质数是 2
    if n < 2:
        return 0

    isPrime = [1] * n # 存放n个元素列表，1表示质数，0表示合数
    isPrime[0] = isPrime[1] = 0   # 0和1不是质数，先排除掉

    # 埃式筛，把不大于根号n的所有质数的倍数剔除
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]: # 判断i是否已经被赋值为0，若为0则不操作
            # 列表切片赋值
            isPrime[i*i:n:i] = [0] * ((n - 1 - i*i) // i + 1)

    return sum(isPrime)

print(countPrimes(10))