class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seenLetts = {}
        l = 0
        res = 0
        maxF = 0

        for r in range(len(s)):
            seenLetts[s[r]] = seenLetts.get(s[r], 0) + 1
            maxF = max(maxF, seenLetts[s[r]])

            while (r - l + 1) - maxF > k:
                seenLetts[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        return res

