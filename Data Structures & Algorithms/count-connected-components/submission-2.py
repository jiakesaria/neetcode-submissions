class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #1. adj list 
        hashmap = defaultdict(list)
        for u, v in edges:
            hashmap[u].append(v)
            hashmap[v].append(u)
        
        #print(hashmap) 

        visited = set()

        res = 0

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for v in hashmap[node]:
                dfs(v)

        for node in range(n): 
            if len(visited) == n:
                return res 
            if node in visited:
                continue
            dfs(node)
            res += 1 
        
        return res 
            
            
