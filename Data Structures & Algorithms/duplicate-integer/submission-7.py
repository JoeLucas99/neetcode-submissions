class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for i in nums:
            mySet.add(i)
        if len(mySet) == len(nums):
            return False
        else:
            return True
