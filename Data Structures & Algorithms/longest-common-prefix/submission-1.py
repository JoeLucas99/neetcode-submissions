class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
            
 ## I think the runtime of this is O(n * m) where n is the length of 
 ## length of the first string and m is the amount of words in the strings array, 
 ## and the and space complexity O(n) because were making a new sting that can be 
 ## as long as the lonest string in the list