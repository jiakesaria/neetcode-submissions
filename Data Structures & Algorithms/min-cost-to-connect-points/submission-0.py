class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # nodes = pt , edges = manhattan dist b/w u and v 
        # dijkstra 
        n = len(points)
        dst = [float("inf")] * n 
        visited = [False] * n
        edges, res, node = 0, 0, 0 
        while edges < n - 1: 
            visited[node] = True 
            nextNode = -1
            for i in range(n):
                if visited[i]:
                    continue
                currd = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                dst[i] = min(dst[i], currd)
                if nextNode == -1 or dst[i] < dst[nextNode]:
                    nextNode = i
            res += dst[nextNode]
            node = nextNode
            edges += 1
                            
        return res