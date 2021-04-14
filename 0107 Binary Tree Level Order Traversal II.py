# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            curl = []
            nextl = []
            for i in queue:
                curl.append(i.val)
                if i.left:
                    nextl.append(i.left)
                if i.right:
                    nextl.append(i.right)
            res.append(curl)
            queue = nextl
        return res[::-1]