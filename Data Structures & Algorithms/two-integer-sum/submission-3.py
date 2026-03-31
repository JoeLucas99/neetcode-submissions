# Given a target int, find the two integers in the array that will create the sum equal to the 
# target integer. Return index of the two integers. 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test1 = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in test1:
                return [test1[diff], i]
            test1[n] = i