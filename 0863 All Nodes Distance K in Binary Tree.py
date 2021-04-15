# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # dfs
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        # bfs
        nodes = [(target, 0)]
        seen = {target}
        res = []
        while nodes:
            node, d = nodes.pop()
            if d == K:
                res.append(node.val)
            for n in (node.left, node.right, node.par):
                if n and n not in seen:
                    seen.add(n)
                    nodes.append((n, d+1))
        return res