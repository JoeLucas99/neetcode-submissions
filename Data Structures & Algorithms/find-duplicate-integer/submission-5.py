class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#Needs to be O(N) time and O(1) Space
#Is an array problem but visualize as a LL
#Use fast slow method to find where the dup node is, break once found
#Make new pointer at same spot as slow. Increment both until they meet again and return slow
        fast , slow = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow