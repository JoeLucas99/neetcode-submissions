class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seenNum = set()
        for num in nums:
            if num in seenNum: return num
            else: seenNum.add(num)
        