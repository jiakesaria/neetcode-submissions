class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False 

        adj = [[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])

        visited = set()

        def dfs(node, par):
            if node in visited: 
                return False
            visited.add(node)
            for n in adj[node]:
                if n == par:
                    continue
                if not dfs(n, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n


        return len(visited) == n
        