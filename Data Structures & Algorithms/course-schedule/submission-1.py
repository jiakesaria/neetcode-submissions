class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adj list 
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(crs, path):
            nonlocal visited 
            if crs in path: 
                return False 
            path.add(crs)
            for pre in preMap[crs]:
                if pre in visited:
                    continue
                if not dfs(pre, path):
                    return False
            path.remove(crs)
            visited.add(crs)
            return True


        for i in range(numCourses):
            if i not in visited:
                cycle = dfs(i, set())
            if not cycle:
                return False
        return True

            
