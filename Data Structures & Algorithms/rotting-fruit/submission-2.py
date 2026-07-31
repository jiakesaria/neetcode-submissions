from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        time = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2 # now rotten
                    fresh -= 1 
                if r > 0 and (r - 1, c) not in visit and grid[r-1][c] != 0:
                    q.append((r - 1, c))
                    visit.add((r - 1, c))
                if r < ROWS - 1 and (r + 1, c) not in visit and grid[r + 1][c] != 0:
                    q.append((r + 1, c))
                    visit.add((r + 1, c))
                if c > 0 and (r, c - 1) not in visit and grid[r][c - 1] != 0:
                    q.append((r, c - 1))
                    visit.add((r, c - 1))
                if c < COLS - 1 and (r, c + 1) not in visit and grid[r][c + 1] != 0:
                    q.append((r, c + 1))
                    visit.add((r, c + 1))
            time += 1
        if fresh == 0:
            return time
        else:
            return -1
        