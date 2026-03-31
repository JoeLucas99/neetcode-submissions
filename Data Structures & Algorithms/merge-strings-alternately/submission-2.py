class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1p , w2p = 0, 0
        newWrd = ""
        while w1p < len(word1):
            newWrd += word1[w1p]
            w1p += 1

            if w2p >= len(word2):
                continue
            else:
                newWrd += word2[w2p]
                w2p += 1
            
        while w2p < len(word2):
            newWrd += word2[w2p]
            w2p += 1
        
        return newWrd
        