class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numList = set(nums)
        maxLen = 0
        for num in nums:
            curLen = 1
            while (num + curLen) in numList:
                curLen += 1
            maxLen = max(maxLen, curLen)
        return maxLen
        