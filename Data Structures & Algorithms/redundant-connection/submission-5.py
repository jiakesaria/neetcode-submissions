class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)] #1 to n
        rank = [1] * (n+1)

        def find(n):
            p = par[n]
            while par[p] != p:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            r1, r2 = rank[find(n1)], rank[find(n2)]
            if r1 >= r2:
                par[find(n2)] = find(n1)
                rank[find(n1)] += r2
            else:
                par[find(n1)] = find(n2)
                rank[find(n2)] += r1


        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            else:
                union(u, v)

        return []