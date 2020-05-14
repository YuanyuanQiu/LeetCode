# def arrangeCoins(n):
#     if n == 0:
#         return 0
#     total = 0
#     count = 0
#     while True:
#         if n-total >= count+1:
#             count += 1 # number of staircase
#             total += count
#         else:
#             return count


def arrangeCoins(n):
    for i in range(n+1):
        if i*(i+1)/2==n:
            return i
        if i*(i+1)/2>n:
            return i-1

print(arrangeCoins(5))
        
            