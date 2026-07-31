from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        ans = []
        
        def bfs(row, col):
            q = deque([(row, col)])
            visited = {(row, col)}
            pacific = atlantic = False 
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if r == 0 or c == 0:
                        pacific = True 
                    if r == ROWS - 1 or c == COLS - 1:
                        atlantic = True
                    if r > 0 and (r - 1, c) not in visited and heights[r][c] >= heights[r-1][c]:
                        q.append((r - 1, c))
                        visited.add((r - 1, c))
                    if r < ROWS - 1 and (r + 1, c) not in visited and heights[r][c] >= heights[r+1][c]:
                        q.append((r + 1, c))
                        visited.add((r + 1, c))
                    if c > 0 and (r, c - 1) not in visited and heights[r][c] >= heights[r][c-1]:
                        q.append((r, c - 1))
                        visited.add((r, c - 1))
                    if c < COLS - 1 and (r, c + 1) not in visited and heights[r][c] >= heights[r][c+1]:
                        q.append((r, c + 1))
                        visited.add((r, c + 1))
                if pacific and atlantic:
                    ans.append([row, col])
                    return 

        for r in range(ROWS):
            for c in range(COLS):
                bfs(r, c)
        return ans 