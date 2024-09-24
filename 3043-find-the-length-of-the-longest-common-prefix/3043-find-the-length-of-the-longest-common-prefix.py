class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        d = {}
        for i in arr1:
            s = str(i)
            pre = ""
            for c in s:
                pre += c
                if pre in d:
                    d[pre]+=1
                else:
                    d[pre]=1
        m = 0
        for i in arr2:
            s = str(i)
            pref = ""
            for c in s:
                pref+=c
                if pref in d:
                    m = max(m, len(pref))
        return m
        
        