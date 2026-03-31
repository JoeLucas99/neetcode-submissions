#Return true if the strings contain the same amount of the same letters. Return false if 
# there's any differences.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        checkS, checkT = {}, {}

        for i in range(len(s)):
            checkS[s[i]] = checkS.get(s[i], 0) + 1
            checkT[t[i]] = checkT.get(t[i], 0) + 1
        if checkS == checkT:
            return True
        return False