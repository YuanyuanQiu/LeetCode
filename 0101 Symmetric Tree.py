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