"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            current_level = []
            next_queue = []
            for i in queue:
                current_level.append(i.val)
                if i.children:
                    for j in i.children:
                        next_queue.append(j)
            res.append(current_level)
            queue = next_queue
        return res