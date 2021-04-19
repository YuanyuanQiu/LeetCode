def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    # (node.val, node.left'id, node.right'id):uid
    trees = collections.defaultdict()
    # 这个哈希表的默认值是当前哈希表中元素的个数
    # 这样每个 key 对应的 value 就会是 0, 1, 2, ... 这样，不会有重复。UID 就是要不能重复。
    trees.default_factory = trees.__len__
    # uid:count
    count = collections.Counter()
    ans = []
    def lookup(node):
        if node:
            # unique id for each node
            uid = trees[node.val, lookup(node.left), lookup(node.right)]
            count[uid] += 1
            if count[uid] == 2:
                ans.append(node)
            return uid

    lookup(root)
    return ans