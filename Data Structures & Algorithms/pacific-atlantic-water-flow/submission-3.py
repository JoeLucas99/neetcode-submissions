class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Params of ocean sets and grid
        #DFS(R,c,set,heig): Checks r/c in bound, in sets, or < prevHeigh. Then add to set and go all dir
        #For every row: check first row/pac, then last row/atl
        #For every col: check first col/pac, then last col/atl
        #For r/c, if in both add to res
        #return res

        atl, pac = set(), set()
        rows, cols = len(heights), len(heights[0])
        res = []

        def dfs(r, c, ocean, prev_height):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in ocean or heights[r][c] < prev_height):
                return
            ocean.add((r,c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        for r in range(rows): #Alternates between Pac left wall and atl right wall
            dfs(r, 0, pac, heights[r][0]) #0,0 , 1,0 , 2,0 
            dfs(r, cols - 1, atl, heights[r][cols - 1]) # 0,2, 1,2 , 2,2

        for c in range(cols):#Alternates between Pac top wall and atl bottom wall
            dfs(0, c, pac, heights[0][c]) #0,1 , 0,2 , 0,3
            dfs(rows - 1, c, atl, heights[rows - 1][c]) #2,0 , 2,1 , 2,2
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res
