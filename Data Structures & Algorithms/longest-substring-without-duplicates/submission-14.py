class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenLetts = set()
        maxLength = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seenLetts:
                seenLetts.remove(s[l])
                l += 1
            seenLetts.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength

        