class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1p , w2p = 0, 0
        newWrd = []
        while w1p < len(word1) or w2p < len(word2):
            if w1p < len(word1):
                newWrd.append(word1[w1p])
            if w2p < len(word2):
                newWrd.append(word2[w2p])
            w1p += 1
            w2p += 1
        
        return "".join(newWrd)
        