class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split(" ")
        c = len(searchWord)
        for i,v in enumerate(l):
            if v[:c] == searchWord:
                return i+1
        return -1

        