def isPowerOfFour(num):
    while num>=4:
        if num % 4 != 0:
            return False
        else:
            num /= 4
    return num == 1

print(isPowerOfFour(5))