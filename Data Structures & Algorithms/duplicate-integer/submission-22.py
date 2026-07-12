class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()

        for i in nums:
            if i in seenNums:
                return True
            seenNums.add(i)
        return False
         