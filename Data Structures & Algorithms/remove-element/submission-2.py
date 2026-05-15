class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        amnt = 0
        l, r = 0, len(nums) - 1
        for num in nums:
            if num != val:
                amnt += 1
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            l += 1
        return amnt