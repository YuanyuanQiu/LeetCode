def isBalanced(self, root: TreeNode) -> bool:
    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        else:
            return 1 + max(left, right)

    if depth(root) == -1:
        return False
    else:
        return True