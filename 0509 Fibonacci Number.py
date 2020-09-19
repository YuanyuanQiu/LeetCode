# 递归
def fib(N):
    if N <= 1:
        return N
    
    return fib(N-1)+fib(N-2)


# 迭代
def fib():
    if N <= 1:
        return N
    
    a, b = 0, 1
    for _ in range(N - 1):
        a, b = b, a + b
    return b


print(fib(3))