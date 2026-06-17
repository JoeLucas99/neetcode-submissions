class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #Turn everthing on the edge to another letter
        #Then go through again and change all Os to Xs and all Ts to Os
        rows, cols = len(board), len(board[0])
        seen = set()
        
        def dfs(r, c):
            if (r >= rows or r < 0 or c < 0 or c >= cols or board[r][c] != "O" or (r,c) in seen):
                return
            board[r][c] = "T"
            seen.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols -1]):
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"