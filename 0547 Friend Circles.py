class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = set()
        count = 0

        def dfs(i):
            for j in range(n):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)

        return count