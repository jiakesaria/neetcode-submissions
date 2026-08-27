class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        dist = [[float("inf")] * (k + 2) for _ in range(n)] 
        dist[src][0] = 0
        pq = [(0, src, 0)] #cost, destination, stops it can make

        while pq:
            cost, curr, stops = heapq.heappop(pq)
            if curr == dst:
                return cost 
            if stops == k + 1:
                continue 
            if cost > dist[curr][stops]:
                continue

            for nei, w in adj[curr]:
                new_cost = cost + w
                if new_cost < dist[nei][stops + 1]:
                    dist[nei][stops+1] = new_cost
                    heapq.heappush(pq, (new_cost, nei, stops+1))
        return -1
