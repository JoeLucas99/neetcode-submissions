class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prev = 1 
        for i, num in enumerate(nums):
            res[i] *= prev
            prev *= num
        
        post = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res

#Space: O(n), it is the same length as the input array
#Time: O(n), we're just running two loops over the length of the input array
        