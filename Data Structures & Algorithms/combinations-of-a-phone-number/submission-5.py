class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def build(i, wrd):
            if len(wrd) == len(digits):
                res.append(wrd)
                return
            for char in digitToChar[digits[i]]:
                build(i + 1, wrd + char)
        
        if digits:
            build(0, "")
        return res
        