class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        for i in range(2 * len(nums)):
            ans[i] = nums[i % len(nums)]
        return ans