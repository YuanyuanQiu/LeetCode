# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if len(nestedList) == 0:
            return 0
        maxDepth = -1
        res = []    # 保存每个节点及其深度 
        
        def dfs(L, depth):
            nonlocal maxDepth
            maxDepth = max(depth, maxDepth)
            for item in L:
                if item.isInteger():
                    res.append((item.getInteger(), depth))
                else:
                    dfs(item.getList(), depth+1)
        
        dfs(nestedList, 1)
        total = 0
        # 得到每个节点的深度和最大深度后，就可以计算加权了
        for num, depth in res:
            total += (num * (maxDepth - depth + 1))
        
        return total