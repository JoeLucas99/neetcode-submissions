class Solution:
    def isPal(self, wrd, l, r):
        while l < r:
            if wrd[l] != wrd[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def part(i, cur):
            if i >= len(s):
                res.append(cur.copy())
                return
            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    cur.append(s[i : j + 1])
                    part(j + 1, cur)
                    cur.pop()

        part(0, [])
        return res
