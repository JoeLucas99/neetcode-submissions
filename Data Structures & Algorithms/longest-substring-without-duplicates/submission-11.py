class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenLetts = set()
        l  = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in seenLetts:
                seenLetts.remove(s[l])
                l += 1
            seenLetts.add(s[r])
            currLength = (r - l) + 1
            maxLength = max(maxLength, currLength)

        return maxLength
        