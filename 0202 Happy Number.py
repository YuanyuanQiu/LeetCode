def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    path = []
    while n != 1 and n not in path:
        path.append(n)
        new_n = 0
        for i in str(n):
            new_n += (int(i) ** 2)
        n = new_n
    if n == 1:
        return True
    else:
        return False