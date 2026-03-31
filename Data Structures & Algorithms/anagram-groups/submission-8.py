class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wrdList = defaultdict(list)
        for wrd in strs:
            cKey = [0] * 26
            for c in wrd:
                cKey[ord(c) - ord("a")] += 1
            wrdList[tuple(cKey)].append(wrd)
        return list(wrdList.values())

#The Runtime is O(n * m) because we have to go through every word in the list, n,
# and go through every char in the words, m

#The space complexity is O(n) because wwe have to make a hm and list of all the words
        