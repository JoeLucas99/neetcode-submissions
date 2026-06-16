class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        distance = 0
        seen = set()

        def addcell(r , c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in seen or grid[r][c] == -1):
                return
            seen.add((r,c))
            q.append([r,c])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen.add((r, c))
                    q.append([r, c])
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addcell(r + 1, c)
                addcell(r - 1, c)
                addcell(r, c + 1)
                addcell(r, c - 1)
            distance += 1
