class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        numSet = set(nums)

        for num in numSet:
            currLength = 1
            while (num + currLength) in numSet:
                currLength += 1
            maxLength = max(currLength, maxLength)
        return maxLength