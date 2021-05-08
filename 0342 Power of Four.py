def isPowerOfFour(self, n: int) -> bool:
    while n >= 4:
        if n % 4 != 0:
            return False
        else:
            n /= 4
    return n == 1