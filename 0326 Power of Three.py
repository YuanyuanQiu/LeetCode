def isPowerOfThree(n):
    while n>1:
        if n%3 != 0:
            return False
        else:
            n /= 3
    return n == 1

print(isPowerOfThree(9))