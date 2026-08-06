from collections import defaultdict
import heapq 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # airports - node, ticket - directed edge
        # each edge is used only one - how? use set
        # start node - JFK!

        # adj list - defaultdict(list) - handles lexicographically (sorted before populating the adj list)

        adj = {src: [] for src, dst in tickets}
        tickets.sort(key = lambda x : x[1])
        for src, dst in tickets:
            adj[src].append(dst)
        
        path = ["JFK"]
        used = set()

        def dfs(node):
            if len(path) == len(tickets) + 1: 
                return True
            if node not in adj: 
                return False 
            temp = list(adj[node])
            for i, v in enumerate(temp):
                adj[node].pop(i)
                path.append(v)
                if dfs(v): return True
                adj[node].insert(i, v)
                path.pop()
            return False


        dfs("JFK")
        return path 

    

       
        