class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        l = []
        c = 0
        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            if A[i] in s2 and A[i] != B[i]:
                c += 1
            if B[i] in s1:
                c += 1
            l.append(c)
        return l
        