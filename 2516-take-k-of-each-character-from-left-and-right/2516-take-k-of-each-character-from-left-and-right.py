class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k==0:
            return 0
        d = {"a": 0,"b": 0, "c":0}
        for i in s:
            d[i] = d.get(i, 0)+1
        if d["a"]<k or d["b"]<k or d["c"]<k:
            return -1
        left = 0
        for right in range(len(s)):
            d[s[right]] -= 1
            if d["a"]<k or d["b"]<k or d["c"]<k:
                d[s[left]] += 1
                left += 1
        return len(s) - (right - left + 1)
            
