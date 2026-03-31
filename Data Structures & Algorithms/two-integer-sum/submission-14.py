class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, n in enumerate(nums):
            needed = target - n
            if needed in numMap:
                return [numMap[needed], i]
            numMap[n] = i
        return None
        