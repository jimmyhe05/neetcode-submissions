class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        col_used = set()
        diag_used = set() # row - col
        anti_diag_used = set() # row + col
        queens = {} # row -> col for building the final board

        def backtrack(row: int) -> None:
            if row == n:
                board = []

                for r in range(n):
                    line = "." * queens[r] + "Q" + "." * (n - queens[r] - 1)
                    board.append(line)
                result.append(board)
                return

            for col in range(n):
                if (col in col_used or (row - col ) in diag_used or (row + col) in anti_diag_used):
                    continue

                col_used.add(col)
                diag_used.add(row - col)
                anti_diag_used.add(row + col)
                queens[row] = col

                backtrack(row + 1)

                col_used.remove(col)
                diag_used.remove(row - col)
                anti_diag_used.remove(row + col)
                del queens[row]

        backtrack(0)

        return result