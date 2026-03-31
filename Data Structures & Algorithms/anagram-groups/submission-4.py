class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = defaultdict(list)
        for wrd in strs:
            key = [0] * 26
            for c in wrd:
                key[ord(c) - ord("a")] += 1
            sort[tuple(key)].append(wrd)
        
        return sort.values()
