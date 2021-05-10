def cloneGraph(self, node: 'Node') -> 'Node':
    # 字典node: clone
    lookup = {}

    # 返回该node的clone
    def dfs(node):
        if not node:
            return
        # 若已存在
        if node in lookup:
            return lookup[node]
        # 构建clone并加入字典
        clone = Node(node.val, [])
        lookup[node] = clone
        # 遍历neighbors
        for n in node.neighbors:
            clone.neighbors.append(dfs(n))
        return clone

    return dfs(node)