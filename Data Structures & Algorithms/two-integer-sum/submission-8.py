class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSeen = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in prevSeen:
                return [prevSeen[needed], i]
            prevSeen[num] = i
