class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wrdList = defaultdict(list)
        for wrd in strs: #n words
            wrdKey = [0] * 26
            for c in wrd: #m chars per word
                wrdKey[ord(c) - ord("a")] += 1
            wrdList[tuple(wrdKey)].append(wrd)
        return list(wrdList.values())



#hm[tuple(char val arr)] : lsit of words
#return arr(hm.values)