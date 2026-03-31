class Solution:

    def encode(self, strs: List[str]) -> str:
        codedWord = ""
        for word in strs:
            codedWord += str(len(word)) + "#" + word
        return codedWord

    def decode(self, s: str) -> List[str]:

        decodedWords = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLength = int(s[i:j])
            i = j + 1
            j = i + wordLength
            decodedWords.append(s[i:j])
            i = j
        return decodedWords
