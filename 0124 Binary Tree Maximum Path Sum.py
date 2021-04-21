def maxPathSum(self, root: TreeNode) -> int:
    res = float('-inf')
    def maxGain(node):
        nonlocal res
        if not node:
            return 0
        leftGain = max(maxGain(node.left), 0)
        rightGain = max(maxGain(node.right), 0)
        total = leftGain + node.val + rightGain
        res = max(res, total)
        return node.val + max(leftGain, rightGain)
    maxGain(root)
    return res