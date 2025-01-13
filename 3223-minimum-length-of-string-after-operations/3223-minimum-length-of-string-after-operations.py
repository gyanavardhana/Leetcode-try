class Solution:
    def minimumLength(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        c = 0
        for i in d.keys():
            if d[i] % 2== 0:
                c += 2
            else:
                c += 1
        return c
                