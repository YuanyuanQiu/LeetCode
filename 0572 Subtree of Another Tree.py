# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and isSame(root1.left, root2.left) and isSame(root1.right, root2.right)
    if not root and not subRoot:
        return True
    if not root or not subRoot:
        return False
    return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)