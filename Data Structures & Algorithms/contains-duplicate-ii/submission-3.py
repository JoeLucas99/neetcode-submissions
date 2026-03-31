class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for l in range(len(nums)):
            r = len(nums) - 1
            while l < r:
                if nums[l] == nums[r] and abs(l - r) <= k:
                    return True
                else:
                    r -= 1
        return False

        