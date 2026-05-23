class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numCheck = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in numCheck:
                return [numCheck[needed], i]
            numCheck[num] = i
        