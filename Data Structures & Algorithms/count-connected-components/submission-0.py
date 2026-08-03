class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        1. we don't care about cycles 
        2. run dfs till len(visited) == n 
        3. if edges given -> always start with an adj list 
        4. if edges are undirected each edge is added twice 
        5. per dfs -> count += 1 ; return count 
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        count = 0 
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for nei in adj[node]:
                if nei == parent or nei in visited:
                    continue
                dfs(nei, node)

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1 
        return count 

            
        