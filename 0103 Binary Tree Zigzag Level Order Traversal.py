# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        flag = True
        while queue:
            cur_level = []
            next_level = []
            for i in queue:
                cur_level.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            if flag:
                res.append(cur_level)
                flag = False
            else:
                res.append(cur_level[::-1])
                flag = True
            queue = next_level
        return res