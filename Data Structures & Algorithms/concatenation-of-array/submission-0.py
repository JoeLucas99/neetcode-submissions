class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hm = {}
        for i, c in enumerate(nums):
            hm[i] = c
        newList = [0] * (n * 2)
        for i in range(n):
            newList[i] = hm[i]   
            newList[i + n] = hm[i]
        return newList  