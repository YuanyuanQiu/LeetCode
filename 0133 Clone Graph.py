def cloneGraph(self, node: 'Node') -> 'Node':
    # node: clone
    lookup = {}

    def dfs(node):
        if not node:
            return
        # node本身为clone后的node
        if node in lookup:
            return lookup[node]
        clone = Node(node.val, [])
        lookup[node] = clone
        
        # neighbors为clone后的neighbors
        for n in node.neighbors:
            clone.neighbors.append(dfs(n))
        
        return clone

    return dfs(node)