class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        
        def backtrack(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))

            found = (backtrack(r + 1, c, i + 1) or 
            backtrack(r - 1, c, i + 1) or 
            backtrack(r, c + 1, i + 1) or 
            backtrack(r, c - 1, i + 1))
        
            path.remove((r,c)) # undo, this cell is usable again for different path

            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True


        return False

        