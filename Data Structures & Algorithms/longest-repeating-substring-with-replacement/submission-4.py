class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seenLetts = {}
        res = 0
        l = 0 
        maxF = 0

        for r in range(len(s)):
            seenLetts[s[r]] = 1 + seenLetts.get(s[r], 0)
            maxF = max(maxF, seenLetts[s[r]])

            while (r - l + 1) - maxF > k:
                seenLetts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


        