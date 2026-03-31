class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wrdList = defaultdict(list)
        for wrd in strs:
            cKey = [0] * 26
            for c in wrd:
                cKey[ord(c) - ord("a")] += 1
            wrdList[tuple(cKey)].append(wrd)
        return list(wrdList.values())
        