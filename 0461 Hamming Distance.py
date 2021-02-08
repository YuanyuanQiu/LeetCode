def hammingDistance(self, x: int, y: int) -> int:
    # bin 返回一个整数 int 或者长整数 long int 的二进制表示。
    # ^ 按位异或运算符：当两对应的二进位相异时，结果为1
    return bin(x ^ y).count('1')
