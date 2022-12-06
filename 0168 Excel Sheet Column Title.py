def convertToTitle(self, columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """

    # Z: 26 * (26**0)
    # AZ: 1 * (26**1) + 26 * (26**0)
    # ZY: 26 * (26**1) + 25 * (26**0)

    res = ''
    while columnNumber > 0:
        columnNumber -= 1
        res = chr(columnNumber % 26 + ord("A")) + res
        columnNumber //= 26
    return res