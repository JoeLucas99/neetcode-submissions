class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lettSet = set()
        maxLength = 0
        l , r = 0, 0
        while r < len(s):
            while s[r] in lettSet:
                lettSet.remove(s[l])
                l += 1
            maxLength = max(maxLength, (r - l) + 1)
            lettSet.add(s[r])
            r += 1
        return maxLength
        