class Solution:
    def isPalindrome(self, s: str) -> bool:
        nS = ""
        for c in s:
            if c.isalnum():
                nS += c.lower()
        return nS == nS[::-1]