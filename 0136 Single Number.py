'''
如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位: a⊕0=a
如果我们对相同的二进制位做 XOR 运算，返回的结果是 0: a⊕a=0
XOR 满足交换律和结合律: a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
所以我们只需要将所有的数进行 XOR 操作，得到那个唯一的数字。
'''

def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

print(singleNumber([4,1,2,1,2]))