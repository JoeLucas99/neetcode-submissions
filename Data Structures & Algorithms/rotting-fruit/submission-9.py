class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Dimensions, time, fresh, q, directions
        #See which is fresh and which is rotten. Inc time and append q accordg
        #Run bfs for q and fresh, go every direction (Check status), make them rotten, inc time
        #Return time if no fresh else -1

        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = collections.deque()
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
                    seen.add((r,c))

        def addCell(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in seen or grid[r][c] != 1):
                return
            q.append([r,c])
            seen.add((r,c))
            nonlocal fresh
            fresh -= 1

        while q and fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            time += 1  

        return time if fresh == 0 else -1