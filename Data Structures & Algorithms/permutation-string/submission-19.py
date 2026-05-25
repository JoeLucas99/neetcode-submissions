class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 and not s2: return True
        if not s1 or not s2: return False
        n1 , n2 = len(s1), len(s2)

        if n1 > n2: return False
        charMapS1 , charMapS2 = [0] * 26, [0] * 26
        
        for i in range(n1):
            charMapS1[ord(s1[i]) - ord("a")] += 1
            charMapS2[ord(s2[i]) - ord("a")] += 1
        if charMapS1 == charMapS2: return True

        for i in range(n1, n2):
            charMapS2[ord(s2[i - n1]) - ord("a")] -= 1
            charMapS2[ord(s2[i]) - ord("a")] += 1
            if charMapS1 == charMapS2: return True
        return False
        