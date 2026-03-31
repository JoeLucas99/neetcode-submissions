# Take the array nums and return true if there's any duplicate values. False if none

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeats = []
        for n in nums:
            if n in repeats:
                return True
            else:
                repeats.append(n)
        return False