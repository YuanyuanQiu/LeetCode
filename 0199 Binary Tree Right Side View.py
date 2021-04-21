# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        levels = []
        while queue:
            cur_level = []
            next_queue = []
            for i in queue:
                cur_level.append(i.val)
                if i.left:
                    next_queue.append(i.left)
                if i.right:
                    next_queue.append(i.right)
            levels.append(cur_level)
            queue = next_queue
        res = []
        for i in levels:
            res.append(i[-1])
        return res