class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        d = {}
        for s,e in intervals:
            d[s] =d.get(s,0)+1
            d[e] =d.get(e+1,0)-1
        l = sorted(d.keys())
        r,o = 0,0
        for i in l:
            r+=d[i]
            o = max(r,o)
        return o

        

        