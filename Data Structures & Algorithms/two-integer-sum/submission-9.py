class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}
        for i, v in enumerate(nums):
            needed = target - v
            if needed in seenNums:
                return [seenNums[needed], i]
            seenNums[v] = i