class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        c = 0
        for i in words:
            if i[:n] == pref:
                c += 1
        return c
        