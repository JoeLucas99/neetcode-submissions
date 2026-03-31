class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curSS = set()
        longSS = 0

        while r < len(s):
            while r < len(s) and s[r] in curSS:
                curSS.remove(s[l])
                l += 1
            curSS.add(s[r])
            r += 1
            curLen = (r - l)
            longSS = max(longSS, curLen)
        return longSS