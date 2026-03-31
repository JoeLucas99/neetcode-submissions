class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for strg in strs:
            sLen = len(strg)
            newStr += str(sLen) + "*" + strg
        return newStr
    
    def decode(self, s: str) -> List[str]:
        newWrds = []
        i = 0
        while i < (len(s)):
            j = i
            while s[j] != "*":
                j += 1
            sLen = int(s[i:j])
            i = j + 1
            j = i + sLen
            newWrds.append(s[i:j])
            i = j
        return newWrds