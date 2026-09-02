class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = [nums[0], 1]
        for num in nums:
            if num == res[0]:
                res[1] += 1
            else:
                res[1] -= 1
                if res[1] == 0:
                    res = [num, 1]

        return res[0]
        