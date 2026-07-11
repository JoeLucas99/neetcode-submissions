class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_nums = set()
        l = 0
        max_length = 0
        for r in range(len(s)):
            while s[r] in seen_nums:
                seen_nums.remove(s[l])
                l += 1
            seen_nums.add(s[r])
            max_length = max(max_length, (r - l + 1))
        return max_length
        