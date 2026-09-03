class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if (r < 0 or c < 0 or r >=  rows or c >= cols or board[r][c] != "O"):
                return
            
            board[r][c] = "T" # as a temp cell

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)


        for r in range(rows):
            dfs(r, 0) # left
            dfs(r, cols - 1) # right

        for c in range(cols):
            dfs(0, c) # top
            dfs(rows - 1, c) # bottom

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        
