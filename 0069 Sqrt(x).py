def mySqrt(self, x: int) -> int:
    if x <= 1:
        return x
    l, r = 0, x//2 # 平方根不会大于本身的一半（4：等于一半；0,1,2,3：小于一半）
    while l < r:
        mid = l + (r - l + 1) // 2 # 如果 mid 下取整，在区间只有2个数的时候 mid=left，一旦进入分支 [mid..right] 区间不会再缩小，出现死循环
        if mid * mid <= x:
            l = mid
        else:
            r = mid - 1
    return l