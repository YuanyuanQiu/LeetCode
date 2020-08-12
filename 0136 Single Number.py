'''
如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位: a⊕0=a
如果我们对相同的二进制位做 XOR 运算，返回的结果是 0: a⊕a=0
XOR 满足交换律和结合律: a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
所以我们只需要将所有的数进行 XOR 操作，得到那个唯一的数字。
'''

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    for i in nums:
        a ^= i #按位异或运算符：当两对应的二进位相异时，结果为1
    return a

# '''
# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# '''
# from functools import reduce
# def singleNumber(nums):
#     return reduce(lambda x, y: x ^ y, nums)

# print(singleNumber([4,1,2,1,2]))