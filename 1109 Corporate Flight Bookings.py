def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    '''
    把每条预定记录的起始航班i记录为k个座位，终点航班j+1记录为-k个座位
    使用for循环：a[i+1] += a[i]
    '''
    a = [0]*(n+1)   # n+1个航班，+1是为了方便计算（处理边界）
    for i,j,k in bookings:
        a[i-1] += k
        a[j] -= k
    for i in range(n):
        a[i+1] += a[i]

    return a[:-1]