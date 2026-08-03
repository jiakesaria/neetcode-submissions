class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses #pre-reqs
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish, res = 0, []
        while q: 
            node = q.popleft()
            finish += 1
            res.append(node)
            for i in adj[node]:
                indegree[i] -= 1 
                if indegree[i] == 0:
                    q.append(i)
        if finish != numCourses:
            return []
        return res[::-1]





        