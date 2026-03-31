class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        minNum = float("inf")
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                minNum = min(minNum, nums[mid])
                r = mid - 1
            else:
                minNum = min(minNum, nums[mid])
                l = mid + 1
        return minNum
# [4,5,0,1,2,3]
 #  l         r
