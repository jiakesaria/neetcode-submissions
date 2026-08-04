class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)] #1 to n

        def dfs(node, parent):

            if node in visited:
                return True #cycle detected
            visited.add(node)
            for n in adj[node]:
                if n == parent:
                    continue
                if dfs(n, node):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
            if dfs(u, -1):
                return [u, v]
        return []


