class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestSeq = 0
        l, r = 0, 0
        seenAmnt = {}
        curLarge, curLen = 0, 0

        while r < len(s):
            seenAmnt[s[r]] = seenAmnt.get(s[r], 0) + 1
            curLarge = max(curLarge, seenAmnt[s[r]])
            
            while (r - l + 1) - curLarge > k:
                seenAmnt[s[l]] -= 1
                l += 1

            longestSeq = max(longestSeq, (r - l + 1))
            r += 1
        return longestSeq
