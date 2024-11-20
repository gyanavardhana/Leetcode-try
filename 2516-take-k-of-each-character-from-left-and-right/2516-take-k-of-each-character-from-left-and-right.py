class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0)+1
        if "a" not in d or "b" not in d or "c" not in d:
            return -1
        if d["a"]<k or d["b"]<k or d["c"]<k:
            return -1
        left = 0
        for right in range(len(s)):
            d[s[right]] -= 1
            if d["a"]<k or d["b"]<k or d["c"]<k:
                d[s[left]] += 1
                left += 1
        return len(s) - (right - left + 1)
            
