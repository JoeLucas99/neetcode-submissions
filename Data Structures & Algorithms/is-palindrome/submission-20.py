class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l < len(s) and s[l].isalnum() != True:
                l += 1
            while r > 0 and s[r].isalnum() != True:
                r -= 1
            if l < len(s) and r > 0 and s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True