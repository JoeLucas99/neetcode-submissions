class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numCount = [0] * 3
        for num in nums:
            numCount[num] += 1
        
        index = 0
        for i in range(3):
            while numCount[i]:
                numCount[i] -= 1
                nums[index] = i
                index += 1
                
