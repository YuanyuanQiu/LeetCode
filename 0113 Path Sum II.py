# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def path(history, root):
            if not root:
                return
            history = history + [root.val]
            if not root.left and not root.right:
                if sum(history) == targetSum:
                    res.append(history)
                return
            path(history, root.left)
            path(history, root.right)
        path([], root)
        return res