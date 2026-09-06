class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count = {}
        for num in nums:
            color_count[num] = color_count.get(num, 0) + 1
        
        k = 0
        for i in range(3):
            if i in color_count:
                amnt = color_count[i]
                for j in range(amnt):
                    nums[k] = i
                    k += 1
            

