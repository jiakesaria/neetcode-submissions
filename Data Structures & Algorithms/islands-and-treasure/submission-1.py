from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j)) # starting sources 
                    visited.add((i, j))

        dist = -1
        while q:
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == INF:
                    grid[r][c] = dist
                if grid[r][c] == -1:
                    continue 
                if r > 0 and (r - 1, c) not in visited:
                    q.append((r - 1, c))
                    visited.add((r - 1, c))
                if r < ROWS - 1 and (r + 1, c) not in visited:
                    q.append((r + 1, c))
                    visited.add((r + 1, c))
                if c > 0 and (r, c - 1) not in visited:
                    q.append((r, c - 1))
                    visited.add((r, c - 1))
                if c < COLS - 1 and (r, c + 1) not in visited:
                    q.append((r, c + 1))
                    visited.add((r, c + 1))
            