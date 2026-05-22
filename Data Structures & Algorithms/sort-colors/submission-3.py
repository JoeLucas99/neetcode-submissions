class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numC = [0] * 3 
        for num in nums:
            numC[num] += 1
        ind = 0
        for i in range(3):
            while numC[i]:
                nums[ind] = i
                numC[i] -= 1
                ind += 1
            
                    
        

        