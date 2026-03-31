class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_nums = {}
        for i, num in enumerate(nums):
            if num in seen_nums:
                if abs(i - seen_nums[num]) <= k:
                    return True
            seen_nums[num] = i
        return False

   #     for l in range(len(nums)):
   #         r = len(nums) - 1
   #         while l < r:
   #             if nums[l] == nums[r] and abs(l - r) <= k:
   #                 return True
  #              else:
 #                   r -= 1
#        return False


        