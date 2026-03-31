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
        

#countS[s[c]] = countS.get(s[c], 0) + 1

#s[c] retrieves the character at index c of string s.
#countS.get(s[c], 0) tries to get the value of s[c] from 
#the dictionary countS. If s[c] is not present, it returns 0 
#(the default value).
#+1 increments the count for the character s[c] in the 
#dictionary countS.