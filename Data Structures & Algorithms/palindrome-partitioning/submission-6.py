class Solution:
    def isPal(self, l, r, wrd):
        while l < r:
            if wrd[l] != wrd[r]:
                return False
            r -= 1
            l += 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(i, cur):
            if i >= len(s):
                res.append(cur.copy())
                return cur
            for j in range(i, len(s)):
                if self.isPal(i, j, s):
                    cur.append(s[i:j + 1])
                    dfs(j + 1, cur)
                    cur.pop()

        dfs(0, [])
        return res

        