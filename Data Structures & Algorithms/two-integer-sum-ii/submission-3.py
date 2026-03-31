class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            cS = numbers[l] + numbers[r]
            if cS < target:
                l += 1
            elif cS > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []

        