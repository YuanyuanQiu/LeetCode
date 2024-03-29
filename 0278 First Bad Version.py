def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    l, r = 1, n
    while l < r:
        mid = l + (r - l) // 2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid + 1
    return r