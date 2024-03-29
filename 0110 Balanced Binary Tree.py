def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def height(root):
        if not root:
            return 0
        return max(height(root.left), height(root.right)) + 1

    if not root:
        return True
    return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)