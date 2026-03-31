class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        mL = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (length + num) in numSet:
                    length += 1
                mL = max(mL, length)
        return mL
        