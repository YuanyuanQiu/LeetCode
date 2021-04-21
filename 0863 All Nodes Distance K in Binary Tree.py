# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def parent(node, par=None):
            if node:
                node.par = par
                parent(node.left, node)
                parent(node.right, node)
        parent(root)
        
        # bfs
        queue = [(target, 0)]
        visited = {target}
        res = []
        while queue:
            node, d = queue.pop()
            if d == K:
                res.append(node.val)
            for i in (node.left, node.right, node.par):
                if i and i not in visited:
                    visited.add(i)
                    queue.append((i, d+1))
        return res