class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seenLetts = {}
        maxF = 0
        res = 0

        for r in range(len(s)):
            seenLetts[s[r]] = 1 + seenLetts.get(s[r], 0)
            maxF = max(maxF, seenLetts[s[r]])

            while (r - l + 1) - maxF > k:
                seenLetts[s[l]] = seenLetts.get(s[l], 0) - 1
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res
        