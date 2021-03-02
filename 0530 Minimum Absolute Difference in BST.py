# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nodes = []
        def help(root,nodes):
            nodes.append(root.val)
            if root.left:
                help(root.left,nodes)
            if root.right:
                help(root.right,nodes)
        help(root,nodes)
        nodes.sort()
        res = float('inf')
        for i in range(len(nodes) - 1):
            res = min(nodes[i+1] - nodes[i], res)
        return res

