class Solution:
    def minLength(self, s: str) -> int:
        l = []
        for i in s:
            if l and l[-1]=='A' and i=='B':
                l.pop()
            elif l and l[-1]=='C' and i=='D':
                l.pop()
            else:
                l.append(i)
        return len(l)
        