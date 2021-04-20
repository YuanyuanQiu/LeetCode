# DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)

        return count

# nion-find algorithm
class Solution:
    def findCircleNum(self, M) -> int:
        father = [i for i in range(len(M))]

        def find(a):
            if father[a] != a:
                father[a] = find(father[a])
            return father[a]

        def union(a, b):
            father[find(b)] = find(a)
            return find(b)

        for a in range(len(M)):
            for b in range(a):
                if M[a][b]:
                    union(a, b)
        for i in range(len(M)):
            find(i)
        return len(set(father))