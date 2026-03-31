class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charsInT, charsInS = {}, {}

        for char in t:
            charsInT[char] = charsInT.get(char, 0) + 1
        for char in s:
            charsInS[char] = charsInS.get(char, 0) + 1
        
        return charsInT == charsInS


        