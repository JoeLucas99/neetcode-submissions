class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 , n2 = len(s1), len(s2)
        s1Map, s2Map = [0] * 26, [0] * 26

        if n1 > n2:
            return False

        for i in range(n1):
            s1Map[ord(s1[i]) - ord("a")] += 1
            s2Map[ord(s2[i]) - ord("a")] += 1
        
        if s1Map == s2Map:
            return True
        
        for i in range(n1, n2):
            s2Map[ord(s2[i]) - ord("a")] += 1
            s2Map[ord(s2[i - n1]) - ord("a")] -= 1
            if s1Map == s2Map:
                return True
        return False