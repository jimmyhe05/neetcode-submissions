class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9

        # checks the row
        for row in range(size):
            seen = set()
            
            for spot in board[row]:
                if spot == ".":
                    continue
                
                if spot in seen:
                    return False
                
                seen.add(spot)
        
        # checks for col
        for col in range(size):
            seen = set()

            for row in range(size):
                spot = board[row][col]

                if spot == ".":
                    continue
                
                if spot in seen:
                    return False
                
                seen.add(spot)

        # checks the sub grid 3 x 3

        for box_row in range(0, size, 3):
            for box_col in range(0, size, 3):
                seen = set()

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        spot = board[row][col]

                        if spot == ".":
                            continue

                        if spot in seen:
                            return False

                        seen.add(spot)
        
        return True

