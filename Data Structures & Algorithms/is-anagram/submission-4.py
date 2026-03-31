#return true if string s and t are annagrams. False if not
#Why use hastsets? Becasue it allows me to incremnet, the value, 
#for every character, the key, I come across.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for c in range(len(s)):
            countS[s[c]] = countS.get(s[c], 0) + 1
            countT[t[c]] = countT.get(t[c], 0) + 1 
        return countS == countT