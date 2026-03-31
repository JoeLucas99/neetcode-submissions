class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for stg in strs:
            newStr += str(len(stg)) + "#" + stg
        return newStr

    def decode(self, s: str) -> List[str]:
        newList = []
        i = 0
        while i < (len(s)):
            j = i
            while s[j] != "#":
                j += 1
            wrdLen = int(s[i:j])
            j += 1
            i = j + wrdLen
            newList.append(s[j:i])
            j = i

        return newList


#5#first4#four3#his
#       i 
#  j