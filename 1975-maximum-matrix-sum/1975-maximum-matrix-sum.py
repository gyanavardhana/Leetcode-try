class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        su = 0
        minab = float('inf')
        negcnt = 0
        for row in matrix:
            for x in row:
                minab = min(minab, abs(x))
                if x<0:
                    su += abs(x)
                    negcnt += 1
                else:
                    su += x
        if negcnt % 2 == 0:
            return su
        else:
            return su - (2 * minab)
        