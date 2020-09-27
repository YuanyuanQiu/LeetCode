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
    
	def dfs(left,right):
		# 递归的终止条件是两个节点都为空
		# 或者两个节点中有一个为空
		# 或者两个节点的值不相等
		if not (left or right):
			return True
		if not (left and right):
			return False
		if left.val!=right.val:
			return False
		return dfs(left.left,right.right) and dfs(left.right,right.left)
		# 用递归函数，比较左节点，右节点
	return dfs(root.left,root.right)