class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Change nums in place and return the amnt of elements not equal to val
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l