class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numInd = {}
        for i, num in enumerate(nums):
            if num in numInd:
                if abs(numInd[num] - i) <= k:
                    return True
            numInd[num] = i
        return False
