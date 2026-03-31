class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSpots = {}
        for i, n in enumerate(nums):
            needed = target - n
            if needed in numsSpots:
                return [numsSpots[needed], i]
            numsSpots[n] = i
        