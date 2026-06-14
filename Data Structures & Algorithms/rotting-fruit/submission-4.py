class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Dimensions, time, fresh, q, directions
        #See which is fresh and which is rotten. Inc time and append q accordg
        #Run bfs for q and fresh, go every direction (Check status), make them rotten, inc time
        #Return time if no fresh else -1

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        fresh, time = 0, 0
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row,col))
            time += 1

        return time if fresh == 0 else -1