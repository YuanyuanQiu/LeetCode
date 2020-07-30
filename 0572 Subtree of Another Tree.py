# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    判断 t 是否为 s 的子树的三个条件是或的关系，即：
    1. 当前两棵树相等；
    2. 或者，t 是 s 的左子树；
    3. 或者，t 是 s 的右子树。
    
    '''
    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    '''
    判断两个树是否相等的三个条件是与的关系，即：
    1. 当前两个树的根节点值相等；
    2. 并且，s 的左子树和 t 的左子树相等；
    3. 并且，s 的右子树和 t 的右子树相等。
    '''   
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)