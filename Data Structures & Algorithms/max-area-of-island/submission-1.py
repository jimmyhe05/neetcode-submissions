class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r: int, c: int) -> int:
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited):
                return 0

            visited.add((r, c))
            area = 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                area += dfs(r + dr, c + dc)

            return area

        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area