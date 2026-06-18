class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        seen = set()

        def addCell(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1 or (r,c) in seen):
                return
            nonlocal fresh
            fresh -= 1
            q.append([r,c])
            seen.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    seen.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                addCell(r + 1,c)
                addCell(r - 1,c)
                addCell(r,c + 1)
                addCell(r,c - 1)
            time += 1
        return time if fresh == 0 else -1