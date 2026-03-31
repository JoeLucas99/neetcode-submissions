class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digPlace = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in digPlace:
                return [digPlace[needed], i]
            digPlace[num] = i