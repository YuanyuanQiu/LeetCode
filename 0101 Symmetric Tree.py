def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True
    elif not root.left and not root.right:
        return True
    elif not root.left or not root.right:
        return False
    elif root.left.val != root.right.val:
        return False
    
    def mirror(p,q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        return p.val == q.val and mirror(p.left, q.right) and mirror(p.right, q.left)

    return mirror(root.left, root.right)


def isSymmetric(self, root):
    if not root:
        return True
    def help(p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and help(p.left, q.right) and help(p.right, q.left)
    return help(root.left, root.right)