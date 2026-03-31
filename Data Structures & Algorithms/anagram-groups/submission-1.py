class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterMap = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord("a")] += 1
            letterMap[tuple(count)].append(str)
        return letterMap.values()

        