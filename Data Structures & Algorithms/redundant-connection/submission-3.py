class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)] #1 to n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        cycle = set()
        cycle_start = -1
        def dfs(node, parent):
            nonlocal cycle_start 
            if node in visited:
                cycle_start = node
                return True #cycle detected
            visited.add(node)
            for n in adj[node]:
                if n == parent:
                    continue
                if dfs(n, node):
                    if cycle_start != -1:
                        cycle.add(n)
                    if cycle_start == node:
                        cycle_start = -1
                    return True
            return False

        dfs(1, -1)

        for u, v in edges[::-1]:
            if u in cycle and v in cycle:
                return [u, v]
        return []


