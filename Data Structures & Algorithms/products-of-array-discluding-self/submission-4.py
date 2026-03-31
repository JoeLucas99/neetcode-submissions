class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newNums = [1] * len(nums)
        pre = 1

        for i in range(len(nums)):
            newNums[i] *= pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums) -1, -1, -1):
            newNums[i] *= post
            post *= nums[i]
        
        return newNums