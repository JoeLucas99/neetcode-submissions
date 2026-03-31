class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digPlace = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in digPlace:
                return [digPlace[needed], i]
            digPlace[num] = i

# Time O(n) because we may nened to go thoug te whole array
# Space O(n) becasue we may need to fill the whole hm before getting the 2 numbers that work