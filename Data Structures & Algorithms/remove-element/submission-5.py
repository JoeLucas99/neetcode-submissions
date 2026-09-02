class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Change nums in place and return the amnt of elements not equal to val
        amnt = 0
        for num in nums:
            if num != val:
                amnt += 1
        nums.sort()
        l, r = 0, len(nums) -1 
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            else:
                l += 1
        return amnt
        