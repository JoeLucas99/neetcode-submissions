class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = defaultdict(list)
        
        for wrd in strs:
            charKey = [0] * 26
            for c in wrd:
                charKey[ord("a") - ord(c)] += 1
            charMap[tuple(charKey)].append(wrd)
        
        return list(charMap.values())