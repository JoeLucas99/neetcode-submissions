class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1 for i in range(len(nums))]
        pre = 1

        for i in range(len(nums)):
            products[i] *= pre
            pre *= nums[i]
        
        post = 1

        for i in range(len(nums) -1, -1, -1):
            products[i] *= post
            post *= nums[i]

        return products


        