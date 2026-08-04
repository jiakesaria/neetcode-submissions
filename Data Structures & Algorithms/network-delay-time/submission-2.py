from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        dist = {i: float("inf") for i in range(n + 1)}
        dist[k] = 0
        pq = [(0, k)]
        visited = set()
        k = 0

        while pq:
            d, u = heapq.heappop(pq)

            if u in visited:
                continue

            visited.add(u)
            k = d

            for nei, t in adj[u]:
                if nei not in visited and (d + t) < dist[nei]:
                    dist[nei] = d + t
                    heapq.heappush(pq, (dist[nei], nei))
        return -1 if len(visited) != n else k
               