class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = {}
        for i, v in enumerate(s):
            if v in d:
                d[v].append(i)
            else:
                d[v] = [i]
        l = []
        for i in d.values():
            if len(i) > 1:
                l.append([min(i), max(i)])
        res = 0
        for st, en in l:
            unq = set(s[st + 1 : en])
            res += len(unq)
        return res
