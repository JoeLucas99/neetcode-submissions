class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newList = [0] * (n * 2)
        for i in range(n):
            newList[i] = nums[i]   
            newList[i + n] = nums[i]
        return newList  