def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    
    # 叶子节点是两个孩子都为null的节点
    if not root.left and not root.right:
        return 1

    # 其中一个为null
    min_depth = 10**9
    if root.left:
        min_depth = min(self.minDepth(root.left), min_depth)
    if root.right:
        min_depth = min(self.minDepth(root.right), min_depth)
    
    return min_depth + 1