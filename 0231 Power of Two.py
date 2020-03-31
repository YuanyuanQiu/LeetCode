def isPowerOfTwo(n):
    if n == 0:
        return False
    result = True
    while n%2 == 0:
        n /= 2
    return n == 1

print(isPowerOfTwo(0))

