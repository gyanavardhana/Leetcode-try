class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        d2 = {}
        for i in s1:
            d2[i] = d2.get(i, 0)+1
        i,j = 0,0
        k = len(s1)
        n = len(s2)
        while j<n:
            d1[s2[j]] = d1.get(s2[j], 0)+1
            j += 1
            if j-i == k:
                if d1==d2:
                    return True
                d1[s2[i]] -= 1
                if d1[s2[i]] == 0:
                    del d1[s2[i]]
                i+=1
        return False
        
        