class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numStorage = {}

        for i, n in enumerate(nums):
            needed = target - n
            if needed in numStorage:
                return [numStorage[needed], i]
            else:
                numStorage[n] = i
        return -1