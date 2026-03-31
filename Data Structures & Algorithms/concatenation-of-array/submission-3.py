class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        r = 0
        while r < len(nums):
            ans[r] = nums[r]
            r += 1
        l = 0
        while r < len(ans):
            ans[r] = nums[l]
            l += 1
            r += 1

        return ans        