class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        out = []
        step = 1 if k > 0 else -1
        k = abs(k)
        
        for i in range(n):
            s = 0
            for j in range(1, k + 1):
                s += code[(i + step * j) % n]
            out.append(s)
        
        return out
        