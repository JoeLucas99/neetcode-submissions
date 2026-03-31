class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longestSeq = 0

        for n in nums:
            currSeq = 0
            if (n - 1) not in seq:
                currSeq = 1
                while (n + currSeq) in seq:
                    currSeq += 1
                longestSeq = max(longestSeq, currSeq)
        return longestSeq

        