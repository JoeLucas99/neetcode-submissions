class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        q = collections.deque()
        distance = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))
        
        def dist(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in seen or grid[r][c] == -1):
                return
            q.append((r,c))
            seen.add((r,c))
        
        while q:
            for i in range(len(q)):
                r , c = q.popleft()
                grid[r][c] = distance
                dist(r + 1, c)
                dist(r -1, c)
                dist(r, c + 1)
                dist(r, c - 1)
            distance += 1
