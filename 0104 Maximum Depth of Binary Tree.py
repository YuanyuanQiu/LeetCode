def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    ans = 1
    return ans + max(self.maxDepth(root.left), self.maxDepth(root.right))