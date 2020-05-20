'''
n-1个元素+1 <===> 1个元素-1
因此，为了让所有元素相等，
只需要将除了最小元素外的所有元素减到最小元素为止
也就是将问题转化为：对所有元素到最小元素的差进行求和
'''

def minMoves(self, nums):
    min_elem=min(nums)
    count=0
    for i in nums:
        count+=i-min_elem
    return count