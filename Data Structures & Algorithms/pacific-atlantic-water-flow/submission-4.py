class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Params of ocean sets and grid
        #DFS(R,c,set,heig): Checks r/c in bound, in sets, or < prevHeigh. Then add to set and go all dir
        #For every row: check first row/pac, then last row/atl
        #For every col: check first col/pac, then last col/atl
        #For r/c, if in both add to res
        #return res

        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()
        res = []

        def dfs(r,c,ocean,prev_height):
            if (r >= rows or r < 0 or c < 0 or c >= cols or heights[r][c] < prev_height or
                (r,c) in ocean):
                return
            ocean.add((r,c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res


        