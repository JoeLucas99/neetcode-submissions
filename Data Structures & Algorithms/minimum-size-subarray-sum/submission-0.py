class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Contract until below
        #minWindow = min(r - l + 1, minWindow)
        #[2,1,5,1,5,3]
        #       l
        #            r

        l = 0
        minWindow = float("inf")
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]

            while curSum >= target:
                minWindow = min(minWindow, r - l + 1)
                curSum -= nums[l]
                l += 1
        if minWindow == float("inf"):
            return 0
        return minWindow
