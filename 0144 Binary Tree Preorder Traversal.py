# recursion
def preorderTraversal(self, root: TreeNode) -> List[int]:
    def preorder(root):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    
    res = []
    preorder(root)
    return res