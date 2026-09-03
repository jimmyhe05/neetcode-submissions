class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r: int, c: int, visited: set, previous_height: int) -> None:
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < previous_height):
                return
            
            visited.add((r, c))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(dr + r, dc + c, visited, heights[r][c])


        # top and bottom row
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c]) # top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c]) # bottom row

        # left and right column 
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0]) # left column
            dfs(r, cols - 1, atlantic, heights[r][cols - 1]) # right column

        return [list(cell) for cell in pacific & atlantic]