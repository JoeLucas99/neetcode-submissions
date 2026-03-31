class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for n1Ind, n1 in enumerate(nums):
            if nums[n1Ind - 1] == n1 and n1Ind > 0:
                    continue
            for n2Ind in range(n1Ind + 1, len(nums) - 1):
                if nums[n2Ind] == nums[n2Ind - 1] and n2Ind > n1Ind + 1:
                    continue
                l , r = n2Ind + 1, len(nums) - 1
                while l < r:
                    curSum = n1 + nums[n2Ind] + nums[l] + nums[r]
                    if curSum < target:
                        l += 1
                    elif curSum > target:
                        r -= 1
                    else:
                        res.append([n1, nums[n2Ind], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res

        