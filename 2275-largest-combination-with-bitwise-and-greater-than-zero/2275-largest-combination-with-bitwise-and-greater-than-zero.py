class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        l = 0
        for i in range(24):
            lar=[]
            for j in candidates:
                lar.append((j>>i) & 1)
            l = max(l,sum(lar))
        return l
        