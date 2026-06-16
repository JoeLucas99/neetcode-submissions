class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in seen or grid[r][c] == 0):
                return 0
            seen.add((r,c))
            res = 1 + (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        return area
        