def sumOfLeftLeaves(self, root: TreeNode) -> int:
    # 叶子树：左子树和右子树都不存在
    if not root:
        return 0
    res = 0
    if root.left and not root.left.left and not root.left.right:
        res += root.left.val
    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) + res