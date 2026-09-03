class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                cand = nums[i]
            cnt += 1 if nums[i] == cand else -1
        return cand