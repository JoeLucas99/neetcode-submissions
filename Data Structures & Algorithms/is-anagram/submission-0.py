#If s and t are anagrams then return true.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            #Anas must be same length, so if not return false.
            return False
        
        test1, test2 = {}, {}
# Create hashmaps to store the char as the key and amount
# of times it appears as the values.
        for i in range(len(s)):
# Iterate through the length of the string. Both same length.
# 'in range' must be on an int. So use len() on string.
            test1[s[i]] = 1 + test1.get(s[i], 0)
            test2[t[i]] = 1 + test2.get(t[i], 0)
# test1, the hm, is the string. So the keys are the chars.
# In hm char at index i in str s, add 1.
# .get is necessary to get key. 
        return test1 == test2

