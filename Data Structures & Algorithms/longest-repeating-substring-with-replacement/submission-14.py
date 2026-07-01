class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxWindow, maxC = 0, 0, 0
        charCount = {}
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            maxC = max(maxC, charCount[s[r]])
            if (r - l + 1) - maxC > k:
                charCount[s[l]] = charCount.get(s[l], 0) - 1
                l += 1
            
            maxWindow = max(maxWindow, (r - l + 1))
        return maxWindow



        