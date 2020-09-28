def isBalanced(self, root: TreeNode) -> bool:
    def height(root: TreeNode) -> int:
        if not root:
            return 0

        leftHeight = height(root.left)
        rightHeight = height(root.right)
        # 不平衡条件：左右子树是否平衡，以当前节点为根的子树是否平衡
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1

    return height(root) >= 0