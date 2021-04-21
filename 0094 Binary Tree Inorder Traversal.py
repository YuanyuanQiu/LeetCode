# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion递归
def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    def dfs(root):
        if not root:
            return
        # 按照 左-打印-右的方式遍历	
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)
    dfs(root)
    return res


# Iteration迭代
def inorderTraversal(self, root):
    res = []
    queue = []
    while root or queue:
        # 不断往左子树方向走，每走一次就将当前节点保存到栈中
        # 这是模拟递归的调用
        if root:
            queue.append(root)
            root = root.left
        # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
        # 然后转向右边节点，继续上面整个过程
        else:
            tmp = queue.pop()
            res.append(tmp.val)
            root = tmp.right
    return res