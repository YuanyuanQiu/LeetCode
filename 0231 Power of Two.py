def isPowerOfTwo(n):
    if n == 0:
        return False

    while n % 2 == 0: # while remainder = 0
        n /= 2

    return n == 1

print(isPowerOfTwo(0))

