class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupNums = set()
        for num in nums:
            if num not in dupNums:
                dupNums.add(num)
            else:
                return True
        return False

