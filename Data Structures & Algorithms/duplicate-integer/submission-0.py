# Take the array nums and return true if there's any duplicate values. False if none

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        testSet = set()

        for i in nums:
            for n in testSet:
                if i == n:
                    return True
            testSet.add(i)
        return False
