class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords = defaultdict(list)

        for wrd in strs:
            numKey = [0] * 26
            for c in wrd:
                numKey[ord(c) - ord("a")] += 1
            sortedWords[tuple(numKey)].append(wrd)
        return list(sortedWords.values())

        