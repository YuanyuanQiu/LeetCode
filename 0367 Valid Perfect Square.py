def isPerfectSquare(num):
    if num < 2:
        return True
    left,right = 2,num//2
    while left <= right:
        mid = left+(right-left)//2
        if mid**2 == num:
            return True
        elif mid**2 > num:
            right = mid-1
        else:
            left = mid+1
    return False

print(isPerfectSquare(16))