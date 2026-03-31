# For an array of nums and a tagert int, return the indexes of the 
# 2 nums that sum to the target int.

# Need to make a hashmap to add the nums to. Then enumerate 
# through and check if you can find the diffrerence
# of the current i and target in the hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {} # Map val to index of where nums appear at.
        for i, n in enumerate(nums):
#For i,index, and n,num, enumerate through nums
            diff = target - n
#Diff = target - number
            if diff in prevNums:
#If diff is found in prevNums hm return indexes.
                return [prevNums[diff], i]
            prevNums[n] = i
#If not found then replace n with i and check again.