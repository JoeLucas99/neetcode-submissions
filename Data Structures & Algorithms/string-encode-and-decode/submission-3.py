class Solution:

    def encode(self, strs: List[str]) -> str:
        newWrd = ''
        for wrd in strs:
            newWrd += str((len(wrd))) + '#' + wrd
        return newWrd

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            wrdLen = int(s[i:j])
            i = j + 1
            j = i + wrdLen
            res.append(s[i:j])
            i = j
        return res