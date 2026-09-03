class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for strg in strs:
                if i >= len(strg) or strs[0][i] != strg[i]:
                    return res
            res += strg[i]
        return res