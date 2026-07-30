class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        def dfs(i, j):
            if (i, j) not in visited:
                visited.add((i, j))
                if i < len(grid) - 1 and grid[i+1][j] == "1":
                    dfs(i + 1, j)
                if i > 0 and grid[i-1][j] == "1":
                    dfs(i - 1, j)
                if j > 0 and grid[i][j-1] == "1":
                    dfs(i, j - 1)
                if j < len(grid[0]) - 1 and grid[i][j+1] == "1":
                    dfs(i, j + 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j) #land 
                    islands += 1 
        return islands 
        