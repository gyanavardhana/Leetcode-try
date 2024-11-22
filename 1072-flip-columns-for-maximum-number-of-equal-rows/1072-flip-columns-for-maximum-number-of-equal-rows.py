class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = {}
        for r in matrix:
            first = r[0]
            cc = ""
            for i in r:
                if i == first:
                    cc += '1'
                else:
                    cc += '0'
            d[cc] = d.get(cc,0)+1
        return max(d.values(),default=0)
        