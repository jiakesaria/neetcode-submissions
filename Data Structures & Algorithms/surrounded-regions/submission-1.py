from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            visited.add((r, c))
            if board[r][c] == 'O': #else == T - visited, == 'X' -> break
                board[r][c] = 'T'
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < ROWS and 0 <= nc < COLS) and (nr, nc) not in visited:
                        dfs(nr, nc)


        for r in range(ROWS): # m * n 
                for c in range(COLS):
                    if ((r == 0 or r == ROWS - 1) or (c == 0 or c == COLS -1)) and board[r][c] == 'O':
                        dfs(r, c)

        for r in range(ROWS): # m * n 
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

        