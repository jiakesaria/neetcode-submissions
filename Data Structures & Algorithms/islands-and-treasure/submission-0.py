from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs(i, j):
            q = deque([(i, j)])
            visited = {(i, j)}
            dist = -1 
            while q:
                dist += 1 
                for _ in range(len(q)):
                    node = q.popleft()
                    if grid[node[0]][node[1]] != -1 and grid[node[0]][node[1]] != 0:
                        if node[0] < len(grid) - 1:
                            if (node[0] + 1, node[1]) not in visited and grid[node[0] + 1][node[1]] != -1:
                                visited.add((node[0] + 1, node[1]))
                                q.append((node[0] + 1, node[1]))

                        if node[0] > 0:
                            if (node[0] - 1, node[1]) not in visited and grid[node[0] - 1][node[1]] != -1:
                                visited.add((node[0] - 1, node[1]))
                                q.append((node[0] - 1, node[1]))

                        if node[1] > 0:
                            if (node[0], node[1] - 1) not in visited and grid[node[0]][node[1] - 1] != -1:
                                visited.add((node[0], node[1] - 1))
                                q.append((node[0], node[1] - 1))

                        if node[1] < len(grid[0]) - 1:
                            if (node[0], node[1] + 1) not in visited and grid[node[0]][node[1] + 1] != -1:
                                visited.add((node[0], node[1] + 1))
                                q.append((node[0], node[1] + 1))
                    elif grid[node[0]][node[1]] == -1:
                        continue
                    else: #treasure found
                        grid[i][j] = dist 
                        return 

        for i in range(len(grid)): #m
            for j in range(len(grid[0])): #n
                if grid[i][j] == 2147483647: #land
                    bfs(i, j)

        
        