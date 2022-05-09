def addBinary(self, a: str, b: str) -> str:
    return '{:b}'.format(int(a, base=2) + int(b, base=2))