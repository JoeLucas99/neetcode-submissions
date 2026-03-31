class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sKeys = {}
        tKeys = {}

        for c in s:
            sKeys[c] = sKeys.get(c, 0) + 1
        for c in t:
            tKeys[c] = tKeys.get(c, 0) + 1
        if tKeys == sKeys:
            return True
        else:
            return False

