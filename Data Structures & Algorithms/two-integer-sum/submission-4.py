class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkedNums = {}
        res = []

        for i, n in enumerate(nums):
            diff = target - n
            if diff in checkedNums:
                res.append(checkedNums[diff])
                res.append(i)
                return res
            checkedNums[n] = i
        