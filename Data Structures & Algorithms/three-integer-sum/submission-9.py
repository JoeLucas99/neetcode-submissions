class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and v == nums[i - 1]:
                continue
            l , r = i + 1 , len(nums) - 1
            while l < r:
                cS = nums[l]+ nums[r] + v
                if cS < 0:
                    l += 1
                elif cS > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], v])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res