class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        newP = 0
        while True:
            slow = nums[slow]
            newP = nums[newP]
            if slow == newP: return slow

        